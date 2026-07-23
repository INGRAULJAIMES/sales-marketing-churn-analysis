# ============================================================
#  CONFIGURACIÓN DEL PROYECTO
# ============================================================
import os

# -------------------- RUTAS DE DATOS --------------------
# Ruta raíz del proyecto (se asume que este script está en src/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Datos crudos (originales)
RAW_DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'raw', 'sales_marketing_raw.csv')

# Datos intermedios (limpios)
INTERIM_DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'interim', 'sales_marketing_clean.csv')

# Datos procesados (listos para modelado)
PROCESSED_DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'processed', 'sales_marketing_processed.csv')

# Artefactos para modelado (train/test split)
X_TRAIN_PATH = os.path.join(PROJECT_ROOT, 'data', 'processed', 'X_train.pkl')
X_TEST_PATH  = os.path.join(PROJECT_ROOT, 'data', 'processed', 'X_test.pkl')
Y_TRAIN_PATH = os.path.join(PROJECT_ROOT, 'data', 'processed', 'y_train.pkl')
Y_TEST_PATH  = os.path.join(PROJECT_ROOT, 'data', 'processed', 'y_test.pkl')

# -------------------- CONFIGURACIÓN DE KAGGLE --------------------
KAGGLE_DATASET = "bhaskerpaul/sales-and-marketing-dataset"
EXPECTED_FILENAME = "Sales - Marketing customer dataset.csv"

ENCODING = None
SEPARATOR = None
CHUNK_SIZE = None
SAMPLE_ROWS = None
AUTO_CONVERT_DATES = True
AUTO_CLEAN_CURRENCY = True

# -------------------- PARÁMETROS GENERALES --------------------
RANDOM_STATE = 42
TEST_SIZE = 0.2          # Proporción para test en train/test split
TARGET_COLUMN = 'churn'  # Nombre de la variable objetivo (ajústalo según tu dataset)

# Columnas que se usarán para el modelado (opcional, por ahora vacío)
FEATURES = []