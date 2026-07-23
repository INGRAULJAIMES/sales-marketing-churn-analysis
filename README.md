# Sales & Marketing Churn Analysis

<!-- Badges -->
[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.3-blue.svg)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.9.0-orange.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-3.0.0-red.svg)](https://xgboost.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-20BEFF.svg)](https://www.kaggle.com/datasets/bhaskerpaul/sales-and-marketing-dataset)
[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange.svg)](https://jupyter.org/)

---

**Un proyecto de ciencia de datos para predecir el abandono de clientes (churn) utilizando técnicas avanzadas de EDA, ingeniería de características y modelado predictivo.**

Este repositorio forma parte de mi portafolio para la **Maestría en Estadística Aplicada y Ciencia de Datos**. Demuestra habilidades en limpieza de datos, análisis exploratorio, preparación de datos y preparación para modelado.

---

## 📖 Tabla de Contenidos

- [🎯 Problema de Negocio](#-problema-de-negocio)
- [❓ Preguntas Clave de Negocio](#-preguntas-clave-de-negocio)
- [📊 Dataset](#-dataset)
- [📈 Antes vs. Después (Calidad de Datos)](#-antes-vs-después-calidad-de-datos)
- [🔍 Data Understanding – Hallazgos Clave](#-data-understanding--hallazgos-clave)
- [📊 Insights de Negocio](#-insights-de-negocio)
- [📊 Visualizaciones Clave](#-visualizaciones-clave)
- [⚙️ Preparación de Datos](#️-preparación-de-datos)
- [🚀 Estado Actual del Proyecto](#-estado-actual-del-proyecto)
- [🔮 Próximos Pasos](#-próximos-pasos-modelado-predictivo)
- [🛠️ Tecnologías y Requisitos](#️-tecnologías-y-requisitos)  
- [🛠️ Instalación y Uso](#️-instalación-y-uso)
- [🤝 Cómo Contribuir](#-cómo-contribuir)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [📄 Licencia](#-licencia)
- [🙌 Autor y Agradecimientos](#-autor-y-agradecimientos)

---

## 🎯 Problema de Negocio

La empresa enfrenta una tasa de **churn (abandono de clientes) del 15%**, lo que representa una pérdida significativa de ingresos recurrentes. El objetivo es **identificar los factores clave que impulsan el churn** y **predecir qué clientes tienen mayor probabilidad de abandonar**, para diseñar estrategias de retención efectivas y basadas en datos.

---

## ❓ Preguntas Clave de Negocio

1. ¿Por qué los clientes abandonan?
2. ¿Qué clientes son más propensos a abandonar?
3. ¿Qué canales de adquisición generan el mayor valor de vida (LTV)?
4. ¿Cómo impacta la satisfacción del cliente en los ingresos?
5. ¿Qué estrategias de marketing reducen el churn?

---

## 📊 Dataset

- **Fuente:** [Sales and Marketing DataSet](https://www.kaggle.com/datasets/bhaskerpaul/sales-and-marketing-dataset) – Kaggle (Bhasker Paul)
- **Filas:** 15,000
- **Columnas:** 30
- **Variable objetivo:** `churn` (binaria, ~85% No churn, ~15% Churn)
- **Problemas incluidos:** valores faltantes, outliers, ruido, tipos mixtos, desbalance de clases

> El dataset fue diseñado para simular un entorno real de CRM y marketing digital, incluyendo datos demográficos, de comportamiento, transaccionales y de satisfacción del cliente.

---

## 📈 Antes vs. Después (Calidad de Datos)

| Métrica | **Antes (Raw)** | **Después (Processed)** | Mejora |
| :--- | :--- | :--- | :--- |
| **Filas** | 15,000 | 15,000 | - |
| **Columnas** | 30 | 52 | +73% (por One‑Hot) |
| **Valores faltantes** | 5 columnas (hasta 40.9%) | **0** | ✅ 100% imputado |
| **Outliers** | Edad negativa, gasto extremo | **Corregidos** | ✅ Winsorización y NaN |
| **Duplicados** | 0 | 0 | ✅ |
| **Tipos de datos** | Mixtos (str, int, float) | **Todos numéricos** | ✅ Codificados y escalados |
| **Desbalance** | 85% / 15% | 85% / 15% | ⚠️ Pendiente de balanceo |

**Visualización de la mejora en calidad:**

| Aspecto | Antes | Después |
| :--- | :--- | :--- |
| **Nulos por columna** | `coupon_code` 40.9% | 0% |
| **Rango de edad** | -4 a 95 | 18 a 95 (corregido) |
| **Escalado** | Sin escalar | `RobustScaler` aplicado |

---

## 🔍 Data Understanding – Hallazgos Clave

| Hallazgo | Descripción |
| :--- | :--- |
| **Umbral Crítico** | Clientes con satisfacción ≤ 2 tienen **50% de probabilidad de abandonar** (vs. 10% si ≥ 3). |
| **Segmentación por Gasto** | La satisfacción es más relevante en clientes de **alto gasto** (ρ ≈ -0.38) que en bajo gasto (ρ ≈ -0.10). |
| **Efecto Directo** | La satisfacción tiene un efecto directo sobre el churn (correlación parcial -0.297). |
| **Sin Multicolinealidad** | Ningún par de predictores supera |0.7|. |
| **Desbalance** | 15.3% churn, lo que requiere técnicas de balanceo. |

---

## 📊 Insights de Negocio

A continuación, se resumen los **hallazgos más relevantes** extraídos del análisis exploratorio de datos. Cada insight está vinculado directamente a una **pregunta de negocio** y respaldado por evidencia cuantitativa.

---

### 1. La satisfacción del cliente es el factor más crítico (y actúa como un umbral)

| Hallazgo | Implicación para el negocio |
| :--- | :--- |
| Los clientes con **satisfacción ≤ 2** tienen un **50% de probabilidad de abandonar**, mientras que aquellos con satisfacción ≥ 3 solo tienen un **10%**. | **La prioridad debe ser evitar que los clientes caigan por debajo del umbral de satisfacción 3.** Un programa de seguimiento proactivo para clientes con puntuaciones bajas podría reducir drásticamente el churn. |

> **Dato clave:** La correlación parcial entre satisfacción y churn (controlando por gasto) es de **-0.297**, lo que confirma un efecto directo y robusto.

---

### 2. El gasto del cliente modera la relación con la satisfacción

| Hallazgo | Implicación para el negocio |
| :--- | :--- |
| La satisfacción es **mucho más relevante** para clientes de **alto gasto** (correlación ≈ -0.38) que para los de **bajo gasto** (correlación ≈ -0.10). | **Las estrategias de retención deben segmentarse por nivel de gasto.** Para clientes de alto valor, la experiencia y la satisfacción son críticas; para los de bajo gasto, otros factores (precio, conveniencia) pueden ser más importantes. |

---

### 3. El desbalance de clases es significativo

| Hallazgo | Implicación para el negocio |
| :--- | :--- |
| El **85%** de los clientes no abandonan, mientras que el **15%** sí lo hace (ratio 5.53:1). | **La métrica de accuracy no es suficiente.** Se deben utilizar métricas como F1‑Score y AUC‑ROC para evaluar modelos. Además, se requiere balanceo de clases (SMOTE o class_weight) para mejorar la detección de clientes en riesgo. |

---

### 4. Los clientes con más tickets de soporte tienden a abandonar más

| Hallazgo | Implicación para el negocio |
| :--- | :--- |
| Los clientes que abandonan tienen, en promedio, **0.5 tickets más** que los activos (2.42 vs 1.92). | **Un aumento en los tickets de soporte es una señal de alerta temprana.** Implementar un sistema de monitoreo que active alertas cuando un cliente supere los 3 tickets podría permitir intervenciones preventivas. |

---

### 5. Los usuarios Premium y con suscripción anual tienen menor churn

| Hallazgo | Implicación para el negocio |
| :--- | :--- |
| Los usuarios **Premium** tienen una tasa de churn **significativamente menor** (~6‑8%) que los no premium (~14‑16%). Los suscriptores **anuales** también muestran menor churn que los mensuales. | **Fomentar la suscripción anual y la membresía premium es una estrategia efectiva de retención.** Ofrecer incentivos para la actualización de planes podría reducir el churn a largo plazo. |

---

### 6. El canal de adquisición no parece influir en el churn

| Hallazgo | Implicación para el negocio |
| :--- | :--- |
| No se observan diferencias significativas en el valor de vida del cliente (LTV) entre los distintos canales de adquisición (Email, Organic, Facebook Ads, Referral, Google Ads). | **La inversión en marketing puede equilibrarse entre canales sin un impacto negativo en la retención.** No hay un canal que claramente atraiga a clientes más leales. |

---

### Resumen ejecutivo para la dirección

| Acción recomendada | Impacto esperado |
| :--- | :--- |
| **Implementar un programa de seguimiento** para clientes con satisfacción ≤ 2. | Reducción del churn en el segmento de alto riesgo. |
| **Segmentar las estrategias de retención** por nivel de gasto. | Mayor efectividad en la retención de clientes de alto valor. |
| **Monitorear el número de tickets de soporte** como señal temprana de abandono. | Intervención proactiva antes de que el cliente se vaya. |
| **Promover la suscripción anual y la membresía Premium.** | Aumento de la lealtad y reducción del churn a largo plazo. |
| **Mantener una inversión equilibrada en todos los canales de adquisición.** | Sin impacto negativo en la retención. |

---

*Estos insights han sido extraídos del análisis de 15,000 registros y validados mediante técnicas estadísticas (correlaciones, umbrales y segmentación).*

---

## 📊 Visualizaciones Clave

| Figura | Descripción | Enlace |
| :--- | :--- | :--- |
| **1. Heatmap de Correlaciones** | Satisfacción y gasto son los factores más relevantes. | [Ver imagen](reports/figures/fig1_correlation_heatmap.png) |
| **2. Perfil del Cliente (Boxplots)** | Churners tienen menor satisfacción y gasto, más tickets de soporte. | [Ver imagen](reports/figures/fig2_churner_profile.png) |
| **3. LTV por Canal** | No hay diferencias significativas entre canales. | [Ver imagen](reports/figures/fig3_ltv_by_channel.png) |
| **4. Satisfacción vs Gasto** | Churners se concentran en baja satisfacción y bajo gasto. | [Ver imagen](reports/figures/fig4_satisfaction_vs_spend.png) |
| **5. Churn por Suscripción y Premium** | Premium y suscripción anual tienen menor churn. | [Ver imagen](reports/figures/fig5_churn_rate_by_segment.png) |

---

## ⚙️ Preparación de Datos

| Etapa | Acción |
| :--- | :--- |
| **Imputación** | `age`, `total_spent`, `satisfaction_score` (mediana por churn), `gender` (moda), `coupon_code` ('Sin cupón'). |
| **Corrección de Outliers** | Edad negativa → NaN e imputada; `total_spent` winsorizado al P99. |
| **Feature Engineering** | Creación de `satisfaction_risk`, `is_high_spender`, interacciones, variables temporales y `revenue_per_visit`. |
| **Codificación** | One‑Hot Encoding de 7 variables categóricas (→ 52 columnas). |
| **Escalado** | `RobustScaler` sobre 16 variables numéricas. |
| **División Train/Test** | Estratificada (80/20) con distribución de churn consistente (15.32% y 15.33%). |

---

## 🚀 Estado Actual del Proyecto

**✅ Fase de Data Preparation completada exitosamente.**

- **Dataset final:** 15,000 filas, 52 columnas, 0 nulos.
- **Splits guardados:** `X_train.pkl`, `X_test.pkl`, `y_train.pkl`, `y_test.pkl` en `data/processed/`.
- **Trazabilidad:** `metadata.json` y `lineage_report.txt` documentan el proceso.

---

## 🔮 Próximos Pasos (Modelado Predictivo)

| Fase | Descripción |
| :--- | :--- |
| **1. Modelos Base** | Regresión Logística y Random Forest. |
| **2. Modelos Avanzados** | XGBoost con GridSearchCV y (opcional) LightGBM. |
| **3. Manejo del Desbalance** | SMOTE o `class_weight='balanced'`. |
| **4. Evaluación** | Accuracy, F1‑Score, AUC‑ROC, Matriz de Confusión, Validación Cruzada. |
| **5. Interpretación** | SHAP o LIME para explicar predicciones. |

---

## 🛠️ Tecnologías y Requisitos

### Tecnologías utilizadas

| Categoría | Tecnología | Versión |
| :--- | :--- | :--- |
| **Lenguaje** | Python | 3.14 |
| **Manipulación de datos** | Pandas | 2.3.3 |
| **Cálculo numérico** | NumPy | 2.3.5 |
| **Visualización** | Matplotlib, Seaborn | 3.10.0, 0.13.2 |
| **Machine Learning** | Scikit-learn | 1.9.0 |
| **Gradient Boosting** | XGBoost | 3.0.0 |
| **Preprocesamiento** | Scikit-learn (RobustScaler, OneHotEncoder) | - |
| **Reportes de EDA** | fg-data-profiling (anteriormente ydata-profiling) | 4.18.4 |
| **Descarga de datasets** | KaggleHub | 1.127.0 |

### Requisitos del sistema

- **Python:** 3.8 o superior (recomendado 3.14).
- **Memoria RAM:** 8 GB mínimo (16 GB recomendado).
- **Espacio en disco:** 500 MB para el proyecto y los datos.
- **Sistema operativo:** Windows, Linux o macOS (probado en Windows 11).

---

## 🛠️ Instalación y Uso

### Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/sales-marketing-churn-analysis.git
cd sales-marketing-churn-analysis
```

## Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
.\venv\Scripts\activate    # Windows
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar los notebooks

1. Abre Jupyter Notebook o VSCode.
2. Ejecuta [`01_CRISP_Data_Understanding.ipynb`](notebooks/01_CRISP_Data_Understanding.ipynb) para el EDA.
3. Ejecuta [`02_CRISP_Data_Preparation.ipynb`](notebooks/02_CRISP_Data_Preparation.ipynb) para la preparación de datos.

## Generar reportes de calidad

```bash
python src/generate_reports.py
```

## Guardar artefactos (splits, metadatos)

```bash
python src/save_artifacts.py
```

## 🤝 Cómo Contribuir

Las contribuciones son bienvenidas. Para reportar errores o sugerir mejoras:

1. Abre un **issue** en GitHub.
2. Haz un **fork** del repositorio y crea una rama (`feature/nueva-funcionalidad`).
3. Envía un **pull request** con una descripción clara de los cambios.

---

## 📁 Estructura del Proyecto

```
sales-marketing-churn-analysis/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   ├── raw/                     # Datos originales (inmutables)
│   ├── interim/                 # Datos limpios, imputados, sin codificar
│   └── processed/               # Datos finales codificados + splits .pkl
├── notebooks/
│   ├── 01_CRISP_Data_Understanding.ipynb
│   └── 02_CRISP_Data_Preparation.ipynb
├── reports/
│   ├── data_understanding_report.md
│   └── figures/                 # 5 visualizaciones clave
├── src/
│   ├── config.py
│   ├── download_dataset.py
│   ├── eda_utils.py
│   ├── generate_reports.py
│   └── save_artifacts.py
└── models/                      # (pendiente para modelos entrenados)
```

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

---

## 🙌 Autor y Agradecimientos

### 👤 Autor

**👋 Hola, soy Raúl Alberto Jaimes**  
*Estudiante de la Maestría en Estadística Aplicada y Ciencia de Datos*  
🎯 Apasionado por el análisis de datos, la estadística y el machine learning aplicado a problemas de negocio.

| Contacto | Enlace |
| :--- | :--- |
| **LinkedIn** | [linkedin.com/in/raul-alberto-jaimes](https://www.linkedin.com/in/raul-alberto-jaimes/) |
| **GitHub** | [github.com/INGRAULJAIMES](https://github.com/INGRAULJAIMES) |

---

### 🚀 Motivación del proyecto

Este proyecto nace de mi interés por aplicar técnicas de ciencia de datos a problemas reales de retención de clientes. El desafío de predecir el churn es común en muchas industrias, y quería demostrar no solo mi capacidad técnica, sino también mi enfoque en **generar insights accionables para la toma de decisiones**.

---

### 🙏 Agradecimientos

- **Bhasker Paul** por crear y compartir el [dataset en Kaggle](https://www.kaggle.com/datasets/bhaskerpaul/sales-and-marketing-dataset), que ha sido fundamental para este proyecto.
- La comunidad de **Kaggle** por su invaluable recurso educativo y la plataforma que permite aprender y experimentar.
- La metodología **CRISP-DM** y las **buenas prácticas de Data Engineering** que han guiado la estructura y el desarrollo del proyecto.

---

### 🤝 ¿Quieres conectar?

Si este proyecto te ha resultado útil, tienes sugerencias o quieres colaborar en algo similar, **no dudes en contactarme a través de LinkedIn**. Estoy abierto a oportunidades, colaboraciones y networking.

---

*Última actualización: 23 de julio de 2026*