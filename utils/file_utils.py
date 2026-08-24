"""
File Utility Functions

Reusable helper functions for reading and
writing project datasets.
"""

from pathlib import Path

import pandas as pd

from config.settings import (
    CSV_SEPARATOR,
    EXPORT_INDEX,
    FILE_ENCODING,
)


def create_directory(
    directory: Path,
) -> None:
    """
    Create a directory if it does not exist.
    """

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )


def read_csv(
    file_path: Path,
) -> pd.DataFrame:
    """
    Read a CSV file.

    Parameters
    ----------
    file_path : Path
        CSV file location.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """

    return pd.read_csv(
        file_path,
        encoding=FILE_ENCODING,
        sep=CSV_SEPARATOR,
    )


def save_csv(
    sales_data: pd.DataFrame,
    output_path: Path,
    index: bool = EXPORT_INDEX,
) -> None:
    """
    Save a DataFrame as a CSV file.

    Parameters
    ----------
    sales_data : pandas.DataFrame
        Dataset to save.

    output_path : Path
        Output file path.

    index : bool
        Whether to export the DataFrame index.
    """

    create_directory(
        output_path.parent,
    )

    sales_data.to_csv(
        output_path,
        index=index,
        encoding=FILE_ENCODING,
        sep=CSV_SEPARATOR,
    )