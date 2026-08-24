"""
Build Date Dimension

This module creates the date dimension from the
analytics sales dataset for use in the Power BI
semantic model.
"""

import pandas as pd

from config.paths import DIM_DATE_FILE
from config.settings import EXPORT_INDEX

from utils.file_utils import save_csv
from utils.logger import get_logger
from utils.validation import validate_analytics_sales_data


logger = get_logger(__name__)


def build_dim_date(
    sales_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build the date dimension.
    """

    start_date = (
        sales_data["InvoiceDate"]
        .min()
        .normalize()
    )

    end_date = (
        sales_data["InvoiceDate"]
        .max()
        .normalize()
    )

    dim_date = pd.DataFrame(
        {
            "Date": pd.date_range(
                start=start_date,
                end=end_date,
                freq="D",
            )
        }
    )

    dim_date["Year"] = (
        dim_date["Date"]
        .dt.year
    )

    dim_date["MonthNumber"] = (
        dim_date["Date"]
        .dt.month
    )

    dim_date["MonthName"] = (
        dim_date["Date"]
        .dt.month_name()
    )

    dim_date["Quarter"] = (
        "Q"
        + dim_date["Date"]
        .dt.quarter.astype(str)
    )

    dim_date["YearMonth"] = (
        dim_date["Date"]
        .dt.strftime("%b-%Y")
    )

    dim_date["MonthStart"] = (
        dim_date["Date"]
        .dt.to_period("M")
        .dt.to_timestamp()
    )

    return dim_date


def run_dim_date() -> None:
    """
    Execute the date dimension pipeline.
    """

    logger.info(
        "Starting date dimension pipeline."
    )

    sales_data = (
        validate_analytics_sales_data()
    )

    logger.info(
        "Analytics dataset loaded (%s records).",
        len(sales_data),
    )

    dim_date = build_dim_date(
        sales_data,
    )

    logger.info(
        "Date dimension contains %s records.",
        len(dim_date),
    )

    save_csv(
        dim_date,
        DIM_DATE_FILE,
        index=EXPORT_INDEX,
    )

    logger.info(
        "Date dimension saved to %s.",
        DIM_DATE_FILE,
    )

    logger.info(
        "Date dimension pipeline completed successfully."
    )


if __name__ == "__main__":
    run_dim_date()