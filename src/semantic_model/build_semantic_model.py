"""
Build Semantic Model

Executes all semantic model pipelines required for
Power BI reporting.
"""

from src.semantic_model.build_dim_date import run_dim_date
from src.semantic_model.build_dim_customer import run_dim_customer

from utils.logger import get_logger


logger = get_logger(__name__)


def run_semantic_model() -> None:
    """
    Execute the semantic model pipeline.
    """

    logger.info(
        "Starting semantic model pipeline."
    )

    run_dim_date()

    run_dim_customer()

    logger.info(
        "Semantic model pipeline completed successfully."
    )


if __name__ == "__main__":
    run_semantic_model()