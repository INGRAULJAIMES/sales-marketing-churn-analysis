# Data Understanding Report - Sales & Marketing Churn Analysis

## 1. Resumen Ejecutivo
El dataset de **Sales and Marketing** (Bhasker Paul) contiene 15,000 registros de clientes con 30 variables. La variable objetivo es `churn` (abandono), con un desbalance significativo (84.7% activos vs 15.3% abandonos). El análisis ha revelado que la relación entre las variables predictoras y el churn **no es lineal**; existe un **umbral crítico en la satisfacción del cliente** (puntuaciones ≤ 2) que multiplica por 5 la tasa de abandono. Además, la importancia de la satisfacción **varía según el nivel de gasto** del cliente: es mucho más relevante para los clientes de alto gasto que para los de bajo gasto.

## 2. Calidad de los Datos
- **Dimensiones:** 15,000 filas, 30 columnas.
- **Valores faltantes:** 
  - `coupon_code` (40.9%) → Tratar como "Sin cupón".
  - `age` (8.0%) → Imputar por mediana (por segmento de churn).
  - `total_spent` (7.0%) → Imputar por mediana (por segmento de churn).
  - `gender` (4.9%) → Imputar por moda.
  - `satisfaction_score` (4.7%) → Imputar por mediana (por segmento de churn).
- **Outliers detectados:**
  - `age`: Valor negativo (-4) → Error de datos. Se corregirá a NaN e imputará.
  - `total_spent`: Valor extremo (15,910 USD) → Posible cliente B2B. Se evaluará winsorización al percentil 99.
- **Duplicados:** 0 duplicados exactos.

## 3. Distribución del Target (Churn)
- **Churn = 0 (Activo):** 12,702 clientes (84.7%)
- **Churn = 1 (Abandonó):** 2,298 clientes (15.3%)
- **Razón mayoría/minoría:** 5.53 → **Desbalance relevante.** Se requiere técnicas de remuestreo (SMOTE) y métricas como F1-Score o AUC-ROC.

## 4. Perfil Demográfico
- **Edad:** Media 35.2 años. Distribución simétrica, con un valor negativo (-4) que debe corregirse.
- **Género:** 46% Male, 45% Female, 10% Other.
- **País y Ciudad:** Distribución balanceada (5 países, 7 ciudades con ~14% cada una). No hay sesgo geográfico evidente.

## 5. Análisis de Comportamiento
- **Soporte:** Los clientes que abandonan tienen ligeramente más tickets de soporte (2.42 vs 1.92). Esta es una diferencia pequeña pero consistente.
- **Otras variables:** Tiempo de sesión, visitas, tasa de apertura de emails y retrasos en entregas muestran diferencias mínimas entre churners y no churners.

## 6. Análisis de Correlaciones (Hallazgos Clave)

### 6.1 Correlaciones Lineales (Spearman)
Las correlaciones máximas son débiles (ninguna supera |0.3|), lo que indica que el churn no se explica bien mediante relaciones lineales simples.

| Variable | Correlación con Churn | Interpretación |
|----------|----------------------|----------------|
| `satisfaction_score` | **-0.262** | La más influyente (aunque débil). |
| `total_spent` | **-0.256** | Segunda más influyente. |
| `support_tickets` | **+0.086** | Asociación muy débil. |
| `delivery_delay_days` | **~0.000** | **Sin relación lineal.** |

### 6.2 Análisis de Umbrales (Hallazgo Revolucionario)
La relación entre satisfacción y churn **no es lineal, sino un efecto escalón**:

| Satisfacción | Tasa de Churn |
|--------------|---------------|
| 1 | **48.7%** |
| 2 | **50.2%** |
| 3 | 9.7% |
| 4 | 8.9% |
| 5 | 9.7% |

**Conclusión:** Existe un **umbral crítico** en satisfacción ≤ 2. Los clientes que puntúan 1 o 2 tienen 5 veces más probabilidad de abandonar que aquellos con puntuación ≥ 3.

### 6.3 Correlaciones por Segmento de Gasto (Heterogeneidad)
La relación entre satisfacción y churn **varía drásticamente según el nivel de gasto**:

| Segmento de Gasto | Correlación (Satisfacción vs Churn) |
|-------------------|-------------------------------------|
| **Alto** | **-0.378** |
| **Medio-Alto** | **-0.390** |
| **Medio-Bajo** | **-0.348** |
| **Bajo** | **-0.096** |

**Conclusión:** La satisfacción es **mucho más relevante** para los clientes de alto gasto. Para los clientes de bajo gasto, la satisfacción apenas influye en el abandono (posiblemente influyan otros factores como el precio).

### 6.4 Correlación Parcial (Efecto Directo)
Se calculó la correlación parcial entre `satisfaction_score` y `churn`, controlando por `total_spent` (gasto total).

- Correlación bruta: **-0.256**
- Correlación parcial: **-0.297**
- **Conclusión:** La satisfacción tiene un **efecto directo y robusto** sobre el churn, independientemente del gasto. Al eliminar la influencia del gasto, el efecto negativo de la insatisfacción se vuelve más fuerte.

### 6.5 Multicolinealidad
No se detectaron pares de variables predictoras con correlación > |0.7|. **Todas las variables numéricas pueden usarse simultáneamente** en modelos lineales sin problemas de inestabilidad.


## 7. Visualizaciones Clave 
- **Figura 1: Heatmap de Correlaciones** – Confirma que satisfacción y gasto son los factores más relevantes.
- **Figura 2: Perfil del Cliente (Boxplots)** – Los churners tienen menor satisfacción y gasto, y ligeramente más tickets de soporte.
- **Figura 3: LTV por Canal de Adquisición** – No se observan diferencias significativas entre canales.
- **Figura 4: Satisfacción vs Gasto (color por churn)** – Los churners se concentran en la zona de baja satisfacción y bajo gasto.
- **Figura 5: Tasa de Churn por Suscripción y Premium** – Los usuarios Premium y con suscripción anual tienen menor churn.

## 8. Preparación de Datos

- Imputación: age, total_spent, satisfaction_score (mediana por churn), gender (moda), coupon_code ('Sin cupón').
- Corrección de outliers: edad negativa → NaN e imputada; total_spent winsorizado al P99.
- Feature Engineering: creación de `satisfaction_risk`, `is_high_spender`, `sat_high_spender`, variables temporales y `revenue_per_visit`.
- Codificación: One‑Hot Encoding de 7 variables categóricas (→ 52 columnas).
- Escalado: RobustScaler sobre 16 variables numéricas.
- Dataset final: 15,000 filas, 52 columnas, 0 nulos.
- División Train/Test estratificada (80/20) con distribución de churn consistente (15.32% y 15.33%).

## 9. Próximos Pasos (Modelado)

- Entrenamiento de modelos: Regresión Logística (línea base), Random Forest, XGBoost.
- Manejo del desbalance: SMOTE o class_weight.
- Evaluación: Accuracy, F1‑Score, AUC‑ROC, Matriz de Confusión.
- Interpretación del modelo ganador mediante SHAP/LIME.