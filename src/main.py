"""
Sales Data Pipeline

Executes the complete sales data pipeline from
raw data ingestion to semantic model creation.
"""

from src.clean.build_clean_sales import run_clean_sales
from src.analytics.build_analytics_sales import run_analytics_sales
from src.semantic_model.build_semantic_model import run_semantic_model

from utils.logger import get_logger


logger = get_logger(__name__)


def main() -> None:
    """
    Execute the complete sales data pipeline.
    """

    logger.info(
        "Starting sales data pipeline."
    )

    run_clean_sales()

    run_analytics_sales()

    run_semantic_model()

    logger.info(
        "Sales data pipeline completed successfully."
    )


if __name__ == "__main__":
    main()
