"""
Project Path Configuration

This module defines all project directories and
file locations used throughout the data pipeline.
"""

from pathlib import Path


# ---------------------------------------------------------
# Project Root
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------
# Project Directories
# ---------------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
CLEAN_DATA_DIR = DATA_DIR / "clean"
ANALYTICS_DATA_DIR = DATA_DIR / "analytics"
SEMANTIC_MODEL_DIR = DATA_DIR / "semantic_model"

LOGS_DIR = PROJECT_ROOT / "logs"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
POWERBI_DIR = PROJECT_ROOT / "powerbi"

SRC_DIR = PROJECT_ROOT / "src"
UTILS_DIR = PROJECT_ROOT / "utils"


# ---------------------------------------------------------
# Data Files
# ---------------------------------------------------------

RAW_SALES_FILE = (
    RAW_DATA_DIR / "online_retail.csv"
)

CLEAN_SALES_FILE = (
    CLEAN_DATA_DIR / "clean_sales.csv"
)

ANALYTICS_SALES_FILE = (
    ANALYTICS_DATA_DIR / "analytics_sales.csv"
)

DIM_DATE_FILE = (
    SEMANTIC_MODEL_DIR / "dim_date.csv"
)

DIM_CUSTOMER_FILE = (
    SEMANTIC_MODEL_DIR / "dim_customer.csv"
)

# ---------------------------------------------------------
# Log Files
# ---------------------------------------------------------

PIPELINE_LOG_FILE = (
    LOGS_DIR / "pipeline.log"
)