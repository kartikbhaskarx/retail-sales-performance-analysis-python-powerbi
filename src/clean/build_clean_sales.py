"""
Clean Sales Dataset

This module transforms the raw sales dataset into a
clean sales dataset by applying the approved
data cleaning rules.
"""

import pandas as pd

from config.paths import CLEAN_SALES_FILE
from config.settings import DATETIME_FORMAT

from utils.file_utils import save_csv
from utils.logger import get_logger
from utils.validation import validate_raw_sales_data


logger = get_logger(__name__)


OPERATIONAL_DESCRIPTIONS = [
    "check",
    "found",
    "Found",
    "adjustment",
    "Manual",
    "amazon",
    "Amazon",
    "?",
    "had been put aside",
]


def remove_duplicates(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Remove duplicate transaction records.
    """

    rows_before = len(sales_data)

    sales_data = (
        sales_data
        .drop_duplicates()
        .reset_index(drop=True)
    )

    logger.info(
        "Removed %s duplicate records.",
        rows_before - len(sales_data),
    )

    return sales_data


def convert_invoice_date(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Convert InvoiceDate to datetime.
    """

    sales_data["InvoiceDate"] = pd.to_datetime(
        sales_data["InvoiceDate"],
        format=DATETIME_FORMAT,
    )

    logger.info(
        "Converted InvoiceDate to datetime."
    )

    return sales_data


def convert_customer_id(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Convert CustomerID to nullable integer.
    """

    sales_data["CustomerID"] = (
        sales_data["CustomerID"]
        .astype("Int64")
    )

    logger.info(
        "Converted CustomerID to nullable Int64."
    )

    return sales_data


def remove_missing_descriptions(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Remove records with missing product descriptions.
    """

    rows_before = len(sales_data)

    sales_data = (
        sales_data
        .dropna(subset=["Description"])
        .reset_index(drop=True)
    )

    logger.info(
        "Removed %s records with missing descriptions.",
        rows_before - len(sales_data),
    )

    return sales_data


def remove_internal_inventory_adjustments(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Remove internal inventory adjustment records
    that are not customer returns.
    """

    rows_before = len(sales_data)

    sales_data = (
        sales_data.loc[
            ~(
                (sales_data["Quantity"] < 0)
                & (
                    ~sales_data["InvoiceNo"]
                    .astype(str)
                    .str.startswith("C")
                )
            )
        ]
        .reset_index(drop=True)
    )

    logger.info(
        "Removed %s internal inventory adjustment records.",
        rows_before - len(sales_data),
    )

    return sales_data


def remove_negative_unit_price(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Remove accounting adjustment records
    with negative unit prices.
    """

    rows_before = len(sales_data)

    sales_data = (
        sales_data.loc[
            sales_data["UnitPrice"] >= 0
        ]
        .reset_index(drop=True)
    )

    logger.info(
        "Removed %s negative unit price records.",
        rows_before - len(sales_data),
    )

    return sales_data


def remove_operational_zero_price_records(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Remove operational records with zero unit price.
    """

    rows_before = len(sales_data)

    sales_data = (
        sales_data.loc[
            ~(
                (sales_data["UnitPrice"] == 0)
                & (
                    sales_data["Description"]
                    .isin(OPERATIONAL_DESCRIPTIONS)
                )
            )
        ]
        .reset_index(drop=True)
    )

    logger.info(
        "Removed %s operational zero-price records.",
        rows_before - len(sales_data),
    )

    return sales_data


def build_clean_sales(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build the clean sales dataset by applying
    all approved cleaning rules.
    """

    sales_data = remove_duplicates(
        sales_data,
    )

    sales_data = convert_invoice_date(
        sales_data,
    )

    sales_data = convert_customer_id(
        sales_data,
    )

    sales_data = remove_missing_descriptions(
        sales_data,
    )

    sales_data = remove_internal_inventory_adjustments(
        sales_data,
    )

    sales_data = remove_negative_unit_price(
        sales_data,
    )

    sales_data = remove_operational_zero_price_records(
        sales_data,
    )

    return sales_data


def run_clean_sales() -> None:
    """
    Execute the clean sales dataset pipeline.
    """

    logger.info(
        "Starting clean sales dataset pipeline."
    )

    sales_data = validate_raw_sales_data()

    logger.info(
        "Raw sales dataset loaded (%s records).",
        len(sales_data),
    )

    sales_data = build_clean_sales(
        sales_data,
    )

    logger.info(
        "Clean sales dataset contains %s records.",
        len(sales_data),
    )

    save_csv(
        sales_data,
        CLEAN_SALES_FILE,
    )

    logger.info(
        "Clean sales dataset saved to %s.",
        CLEAN_SALES_FILE,
    )

    logger.info(
        "Clean sales dataset pipeline completed successfully."
    )


if __name__ == "__main__":
    run_clean_sales()