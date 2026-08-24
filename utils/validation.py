"""
Validation Utilities

Reusable validation functions used throughout the
sales data pipeline.

Validation Flow
---------------
1. Generic validation helpers
2. Raw dataset validation
3. Clean dataset validation
"""

from pathlib import Path

import pandas as pd

from config.paths import (
    RAW_SALES_FILE,
    CLEAN_SALES_FILE,
    ANALYTICS_SALES_FILE,
)

from config.settings import (
    REQUIRED_COLUMNS,
)

from utils.file_utils import (
    read_csv,
)


# ==========================================================
# Generic Validation Helpers
# ==========================================================

def validate_file_exists(
    file_path: Path,
) -> None:
    """
    Validate that a file exists.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )


def validate_dataframe_not_empty(
    sales_data: pd.DataFrame,
) -> None:
    """
    Validate that a DataFrame is not empty.
    """

    if sales_data.empty:
        raise ValueError(
            "Dataset is empty."
        )


def validate_required_columns(
    sales_data: pd.DataFrame,
    required_columns: list[str],
) -> None:
    """
    Validate that all required columns exist.
    """

    missing_columns = [
        column
        for column in required_columns
        if column not in sales_data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )


def validate_datetime_column(
    sales_data: pd.DataFrame,
    column_name: str,
) -> None:
    """
    Validate that a column has datetime dtype.
    """

    if not pd.api.types.is_datetime64_any_dtype(
        sales_data[column_name]
    ):
        raise TypeError(
            f"{column_name} must be datetime."
        )


def validate_integer_column(
    sales_data: pd.DataFrame,
    column_name: str,
) -> None:
    """
    Validate that a column has nullable integer dtype.
    """

    if not pd.api.types.is_integer_dtype(
        sales_data[column_name]
    ):
        raise TypeError(
            f"{column_name} must be Int64."
        )


def validate_no_missing_values(
    sales_data: pd.DataFrame,
    columns: list[str],
) -> None:
    """
    Validate that selected columns contain
    no missing values.
    """

    for column in columns:

        if sales_data[column].isna().any():

            raise ValueError(
                f"{column} contains missing values."
            )


# ==========================================================
# Raw Dataset Validation
# Used by build_clean_sales.py
# ==========================================================

def validate_raw_sales_data() -> pd.DataFrame:
    """
    Validate and load the raw sales dataset.

    Returns
    -------
    pandas.DataFrame
        Validated raw sales dataset.
    """

    validate_file_exists(
        RAW_SALES_FILE,
    )

    sales_data = read_csv(
        RAW_SALES_FILE,
    )

    validate_dataframe_not_empty(
        sales_data,
    )

    validate_required_columns(
        sales_data,
        REQUIRED_COLUMNS,
    )

    return sales_data


# ==========================================================
# Clean Dataset Validation
# Used by build_analytics_dataset.py
# ==========================================================

def validate_clean_sales_data() -> pd.DataFrame:
    """
    Validate and load the clean sales dataset.

    Returns
    -------
    pandas.DataFrame
        Validated clean sales dataset.
    """

    validate_file_exists(
        CLEAN_SALES_FILE,
    )

    sales_data = read_csv(
        CLEAN_SALES_FILE,
    )

    validate_dataframe_not_empty(
        sales_data,
    )

    validate_required_columns(
        sales_data,
        REQUIRED_COLUMNS,
    )

    sales_data["InvoiceDate"] = pd.to_datetime(
        sales_data["InvoiceDate"],
    )

    validate_datetime_column(
        sales_data,
        "InvoiceDate",
    )

    sales_data["CustomerID"] = (
        sales_data["CustomerID"]
        .astype("Int64")
    )

    validate_integer_column(
        sales_data,
        "CustomerID",
    )

    validate_no_missing_values(
        sales_data,
        [
            "InvoiceNo",
            "StockCode",
            "Quantity",
            "InvoiceDate",
            "UnitPrice",
            "Country",
        ],
    )

    return sales_data

# ==========================================================
# Analytics Dataset Validation
# Used by semantic model builders
# ==========================================================

def validate_analytics_sales_data() -> pd.DataFrame:
    """
    Validate and load the analytics sales dataset.

    Returns
    -------
    pandas.DataFrame
        Validated analytics sales dataset.
    """

    validate_file_exists(
        ANALYTICS_SALES_FILE,
    )

    sales_data = read_csv(
        ANALYTICS_SALES_FILE,
    )

    validate_dataframe_not_empty(
        sales_data,
    )

    sales_data["InvoiceDate"] = pd.to_datetime(
        sales_data["InvoiceDate"],
    )

    validate_datetime_column(
        sales_data,
        "InvoiceDate",
    )

    sales_data["CustomerID"] = (
        sales_data["CustomerID"]
        .astype("Int64")
    )

    validate_integer_column(
        sales_data,
        "CustomerID",
    )

    return sales_data