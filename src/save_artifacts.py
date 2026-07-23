# ============================================================
# save_artifacts.py - Guardado de artefactos del proyecto
# ============================================================
# OBJETIVO: Organizar y guardar todos los artefactos generados
# en las Semanas 1 y 2 para garantizar reproducibilidad y
# trazabilidad (Data Lineage).
#
# AUTOR: [Tu nombre]
# FECHA: 2026-07-22
# ============================================================

import os
import pandas as pd
import joblib
import json
from sklearn.model_selection import train_test_split

# --------------------------------------------
# 1. CONFIGURACIÓN DE RUTAS (ESTÁNDAR INDUSTRIA)
# --------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Rutas de las subcarpetas
RAW_DIR = os.path.join(DATA_DIR, "raw")
INTERIM_DIR = os.path.join(DATA_DIR, "interim")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Crear carpetas si no existen (red de seguridad, aunque ya deberían existir por .gitkeep)
for path in [RAW_DIR, INTERIM_DIR, PROCESSED_DIR, MODELS_DIR]:
    os.makedirs(path, exist_ok=True)

print("✅ Estructura de carpetas verificada/creada.")

# --------------------------------------------
# 2. CARGA DEL DATASET PROCESADO (Semana 2)
# --------------------------------------------
# Cargamos el dataset final que generaste en la Semana 2.
processed_file = os.path.join(PROCESSED_DIR, "sales_marketing_processed.csv")

# Si el archivo no existe en processed, buscarlo en la raíz de data/ (por si no se movió)
if not os.path.exists(processed_file):
    fallback_file = os.path.join(DATA_DIR, "processed_data.csv")
    if os.path.exists(fallback_file):
        print("⚠️ Moviendo processed_data.csv a data/processed/...")
        df = pd.read_csv(fallback_file)
        df.to_csv(processed_file, index=False)
    else:
        raise FileNotFoundError("No se encontró el dataset procesado. Asegúrate de haber ejecutado la Semana 2.")

df = pd.read_csv(processed_file)
print(f"✅ Dataset procesado cargado: {df.shape[0]:,} filas, {df.shape[1]} columnas.")

# --------------------------------------------
# 3. SEPARACIÓN X / Y (reproducible)
# --------------------------------------------
target = "churn"
if target not in df.columns:
    raise ValueError(f"La columna '{target}' no existe en el dataset procesado.")

y = df[target]
X = df.drop(columns=[target])

print(f"✅ X: {X.shape}, y: {y.shape}")

# --------------------------------------------
# 4. DIVISIÓN TRAIN/TEST (estratificada, con semilla fija)
# --------------------------------------------
RANDOM_STATE = 42
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)

print(f"✅ Train: {X_train.shape[0]} registros, Test: {X_test.shape[0]} registros")
print(f"   Distribución de churn en train: {y_train.mean():.2%}")
print(f"   Distribución de churn en test: {y_test.mean():.2%}")

# --------------------------------------------
# 5. GUARDADO DE SPLITS (en .pkl para la Semana 3)
# --------------------------------------------
joblib.dump(X_train, os.path.join(PROCESSED_DIR, "X_train.pkl"))
joblib.dump(X_test, os.path.join(PROCESSED_DIR, "X_test.pkl"))
joblib.dump(y_train, os.path.join(PROCESSED_DIR, "y_train.pkl"))
joblib.dump(y_test, os.path.join(PROCESSED_DIR, "y_test.pkl"))
print("✅ Splits guardados en data/processed/ (formato .pkl)")

# --------------------------------------------
# 6. GUARDADO DE METADATOS (para trazabilidad)
# --------------------------------------------
metadata = {
    "dataset_name": "Sales and Marketing Churn",
    "source": "Kaggle (Bhasker Paul)",
    "target_column": target,
    "random_state": RANDOM_STATE,
    "split_ratio": {"train": 0.8, "test": 0.2},
    "features": X.columns.tolist(),
    "shape": {"rows": df.shape[0], "columns": df.shape[1]},
    "date_processed": "2026-07-22",
    "notebook_generation": "02_CRISP_Data_Preparation.ipynb"
}

with open(os.path.join(PROCESSED_DIR, "metadata.json"), "w") as f:
    json.dump(metadata, f, indent=4)
print("✅ Metadatos guardados en data/processed/metadata.json")

# --------------------------------------------
# 7. DOCUMENTACIÓN DE LINEAGE (trazabilidad)
# --------------------------------------------
lineage_report = """
=== DATA LINEAGE REPORT ===

1. Raw Data (Origen):
   - Fuente: Kaggle (bhaskerpaul/sales-and-marketing-dataset)
   - Archivo original: Sales - Marketing customer dataset.csv
   - Ubicación: data/raw/sales_marketing_raw.csv (debe copiarse manualmente)

2. Interim Data (Limpieza básica):
   - Transformaciones aplicadas:
     - Eliminación de duplicados.
     - Imputación de nulos (mediana por churn, moda).
     - Corrección de edad negativa (NaN).
     - Winsorización de total_spent (P99).
   - Ubicación: data/interim/sales_marketing_clean.csv

3. Processed Data (Preparación para ML):
   - Transformaciones aplicadas:
     - Feature Engineering: satisfaction_risk, is_high_spender, interacciones, variables temporales.
     - One-Hot Encoding (7 variables).
     - Escalado con RobustScaler (16 variables).
   - Ubicación: data/processed/sales_marketing_processed.csv

4. Model Input (Splits):
   - X_train.pkl, X_test.pkl, y_train.pkl, y_test.pkl
   - División estratificada (80/20) con semilla 42.

5. Metadata:
   - data/processed/metadata.json
"""

with open(os.path.join(PROCESSED_DIR, "lineage_report.txt"), "w") as f:
    f.write(lineage_report)
print("✅ Informe de trazabilidad (Lineage) guardado.")

print("\n" + "="*70)
print(" 🚀 PROCESO DE GUARDADO DE ARTEFACTOS COMPLETADO EXITOSAMENTE.")
print(" Estructura final:")
print("  data/")
print("  ├── raw/")
print("  │   └── .gitkeep (y raw data si se copia)")
print("  ├── interim/")
print("  │   └── .gitkeep (y clean data si se genera)")
print("  └── processed/")
print("      ├── sales_marketing_processed.csv")
print("      ├── X_train.pkl")
print("      ├── X_test.pkl")
print("      ├── y_train.pkl")
print("      ├── y_test.pkl")
print("      ├── metadata.json")
print("      └── lineage_report.txt")
print("="*70)