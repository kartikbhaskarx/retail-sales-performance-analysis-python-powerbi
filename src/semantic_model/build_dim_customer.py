"""
Build Customer Dimension

This module creates the customer dimension from the
analytics sales dataset for use in the Power BI
semantic model.
"""

import pandas as pd

from config.paths import DIM_CUSTOMER_FILE
from config.settings import EXPORT_INDEX

from utils.file_utils import save_csv
from utils.logger import get_logger
from utils.validation import validate_analytics_sales_data


logger = get_logger(__name__)


def build_dim_customer(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build the customer dimension.
    """

    dim_customer = (
        sales_data.loc[
            sales_data["CustomerID"].notna(),
            [
                "CustomerID",
                "CustomerType",
                "PurchaseFrequency",
                "RepeatCustomer",
            ],
        ]
        .drop_duplicates(
            subset=["CustomerID"],
        )
        .sort_values(
            "CustomerID",
        )
        .reset_index(
            drop=True,
        )
    )

    return dim_customer


def run_dim_customer() -> None:
    """
    Execute the customer dimension pipeline.
    """

    logger.info(
        "Starting customer dimension pipeline."
    )

    sales_data = (
        validate_analytics_sales_data()
    )

    logger.info(
        "Analytics dataset loaded (%s records).",
        len(sales_data),
    )

    dim_customer = build_dim_customer(
        sales_data,
    )

    logger.info(
        "Customer dimension contains %s records.",
        len(dim_customer),
    )

    save_csv(
        dim_customer,
        DIM_CUSTOMER_FILE,
        index=EXPORT_INDEX,
    )

    logger.info(
        "Customer dimension saved to %s.",
        DIM_CUSTOMER_FILE,
    )

    logger.info(
        "Customer dimension pipeline completed successfully."
    )


if __name__ == "__main__":
    run_dim_customer()