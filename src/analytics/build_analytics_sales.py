"""
Analytics Sales Dataset

This module transforms the clean sales dataset into an
analytics-ready dataset by creating business features
used for reporting and dashboarding.
"""

import pandas as pd

from config.paths import ANALYTICS_SALES_FILE

from utils.file_utils import save_csv
from utils.logger import get_logger
from utils.validation import validate_clean_sales_data


logger = get_logger(__name__)


def create_revenue(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create transaction revenue.
    """

    logger.info(
        "Creating revenue field."
    )

    sales_data["Revenue"] = (
        sales_data["Quantity"]
        * sales_data["UnitPrice"]
    )

    return sales_data


def create_time_fields(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create time intelligence features.
    """

    logger.info(
        "Creating time intelligence fields."
    )

    sales_data = sales_data.assign(
        InvoiceYear=sales_data["InvoiceDate"].dt.year,
        InvoiceMonth=sales_data["InvoiceDate"].dt.month,
        MonthName=sales_data["InvoiceDate"].dt.month_name(),
        Quarter=(
            "Q"
            + sales_data["InvoiceDate"]
            .dt.quarter.astype(str)
        ),
        MonthStart=(
            sales_data["InvoiceDate"]
            .dt.to_period("M")
            .dt.to_timestamp()
        ),
        YearMonth=(
            sales_data["InvoiceDate"]
            .dt.strftime("%b-%Y")
        ),
    )

    return sales_data


def create_customer_metrics(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create customer analytical features.
    """

    logger.info(
        "Creating customer metrics."
    )

    sales_data = sales_data.assign(
        CustomerType=sales_data["CustomerID"].apply(
            lambda customer: (
                "Registered Customer"
                if pd.notna(customer)
                else "Guest Customer"
            )
        )
    )

    # Count unique completed Sale invoices per customer
    customer_purchase_frequency = (
        sales_data.loc[
            sales_data["OrderType"].eq("Sale")
            & sales_data["CustomerID"].notna()
        ]
        .groupby("CustomerID")["InvoiceNo"]
        .nunique()
    )

    sales_data["PurchaseFrequency"] = (
        sales_data["CustomerID"]
        .map(customer_purchase_frequency)
    )

    sales_data["RepeatCustomer"] = (
        sales_data["PurchaseFrequency"] > 1
    ).map(
        {
            True: "Repeat Customer",
            False: "One-Time Customer",
        }
    )

    return sales_data


def create_order_metrics(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create order-level analytical features.
    """

    logger.info(
        "Creating order metrics."
    )

    sales_data["OrderType"] = (
        sales_data["InvoiceNo"]
        .astype(str)
        .str.startswith("C")
        .map(
            {
                True: "Cancellation",
                False: "Sale",
            }
        )
    )

    sales_data["InvoiceRevenue"] = (
        sales_data
        .groupby("InvoiceNo")["Revenue"]
        .transform("sum")
    )

    sales_data["BasketSize"] = (
        sales_data
        .groupby("InvoiceNo")["StockCode"]
        .transform("count")
    )

    return sales_data


def build_analytics_sales(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build the analytics-ready sales dataset.
    """

    sales_data = create_revenue(
        sales_data,
    )

    sales_data = create_time_fields(
        sales_data,
    )

    sales_data = create_order_metrics(
        sales_data,
    )

    sales_data = create_customer_metrics(
        sales_data,
    )

    return sales_data


def run_analytics_sales() -> None:
    """
    Execute the analytics sales dataset pipeline.
    """

    logger.info(
        "Starting analytics sales dataset pipeline."
    )

    sales_data = validate_clean_sales_data()

    logger.info(
        "Clean sales dataset loaded (%s records).",
        len(sales_data),
    )

    sales_data = build_analytics_sales(
        sales_data,
    )

    logger.info(
        "Analytics dataset contains %s records.",
        len(sales_data),
    )

    save_csv(
        sales_data,
        ANALYTICS_SALES_FILE,
    )

    logger.info(
        "Analytics dataset saved to %s.",
        ANALYTICS_SALES_FILE,
    )

    logger.info(
        "Analytics dataset pipeline completed successfully."
    )


if __name__ == "__main__":
    run_analytics_sales()