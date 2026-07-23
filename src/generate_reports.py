# ============================================================
# generate_reports.py - Reportes EDA con ydata-profiling
# ============================================================
import os
import pandas as pd
from ydata_profiling import ProfileReport

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

print("=" * 70)
print(" GENERANDO REPORTES EDA CON YDATA-PROFILING")
print("=" * 70)

# --- Reporte RAW ---
raw_path = os.path.join(DATA_DIR, "raw", "sales_marketing_raw.csv")
if os.path.exists(raw_path):
    print("\n📊 [1/2] Generando reporte: DATOS CRUDOS (Antes)")
    df_raw = pd.read_csv(raw_path)
    profile_raw = ProfileReport(df_raw, title="Datos Crudos (Antes)", explorative=True)
    profile_raw.to_file(os.path.join(REPORTS_DIR, "report_raw.html"))
    print("   ✅ Guardado: reports/report_raw.html")
else:
    print("\n⚠️ No se encontró data/raw/sales_marketing_raw.csv")

# --- Reporte PROCESSED ---
proc_path = os.path.join(DATA_DIR, "processed", "sales_marketing_processed.csv")
if os.path.exists(proc_path):
    print("\n📊 [2/2] Generando reporte: DATOS PROCESADOS (Después)")
    df_proc = pd.read_csv(proc_path)
    profile_proc = ProfileReport(df_proc, title="Datos Procesados (Después)", explorative=True)
    profile_proc.to_file(os.path.join(REPORTS_DIR, "report_processed.html"))
    print("   ✅ Guardado: reports/report_processed.html")
else:
    print("\n⚠️ No se encontró data/processed/sales_marketing_processed.csv")

print("\n" + "=" * 70)
print(" 🎯 PROCESO COMPLETADO")
print("   📁 reports/report_raw.html")
print("   📁 reports/report_processed.html")
print("=" * 70)