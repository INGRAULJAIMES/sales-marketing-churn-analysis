# ============================================================
# DESCARGA DEL DATASET DESDE KAGGLE
# ============================================================

import warnings
warnings.filterwarnings('ignore')

import os
import kagglehub
from config import KAGGLE_DATASET

print("Descargando dataset desde Kaggle...")
path = kagglehub.dataset_download(KAGGLE_DATASET)
print(f"Dataset descargado en: {path}")

# Listar archivos disponibles
print("\n--- Archivos disponibles ---")
for dirname, _, filenames in os.walk(path):
    for filename in filenames:
        print(f" - {filename}")