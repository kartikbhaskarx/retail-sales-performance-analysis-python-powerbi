"""
Project Logger

Configure and return a reusable logger for the
sales analytics pipeline.
"""

import logging

from config.paths import (
    LOGS_DIR,
    PIPELINE_LOG_FILE,
)

from config.settings import (
    LOG_DATE_FORMAT,
    LOG_FORMAT,
    LOG_LEVEL,
)


def get_logger(
    logger_name: str = "pipeline",
) -> logging.Logger:
    """
    Return a configured project logger.

    Parameters
    ----------
    logger_name : str, default="pipeline"
        Logger name.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    LOGS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger = logging.getLogger(
        logger_name,
    )

    if logger.handlers:
        return logger

    logger.setLevel(
        LOG_LEVEL,
    )

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )

    file_handler = logging.FileHandler(
        PIPELINE_LOG_FILE,
        encoding="utf-8",
    )
    file_handler.setFormatter(
        formatter,
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        formatter,
    )

    logger.addHandler(
        file_handler,
    )

    logger.addHandler(
        console_handler,
    )

    logger.propagate = False

    return logger