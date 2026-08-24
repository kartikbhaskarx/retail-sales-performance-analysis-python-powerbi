"""
Project Settings

This module contains project-wide configuration values
used throughout the sales analytics pipeline.
"""


# ---------------------------------------------------------
# Project Information
# ---------------------------------------------------------

PROJECT_NAME = "TATA Online Retail Analytics"

PROJECT_VERSION = "1.0.0"


# ---------------------------------------------------------
# CSV Settings
# ---------------------------------------------------------

FILE_ENCODING = "ISO-8859-1"

CSV_SEPARATOR = ","

EXPORT_INDEX = False


# ---------------------------------------------------------
# Raw Dataset Schema
# ---------------------------------------------------------

REQUIRED_COLUMNS = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country",
]


# ---------------------------------------------------------
# Date Settings
# ---------------------------------------------------------

DATETIME_FORMAT = "%d-%m-%Y %H:%M"


# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

LOG_LEVEL = "INFO"

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(module)s | "
    "%(message)s"
)

LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"