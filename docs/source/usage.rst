Usage Guide
================================================================================================

This guide explains how to use the `datalizer` package, covering data loading, preprocessing, and validation.

Loading Data
------------------------------------------------------------------------------------------------

Use `datalizer.loader.load_data` to load datasets in supported formats (`.csv`, `.xlsx`, `.json`):

.. code-block:: python

    import datalizer.loader as dl

    # Load a CSV file
    df = dl.load_data("data.csv")

    # Load an Excel file
    df = dl.load_data("data.xlsx")

    # Load a JSON file
    df = dl.load_data("data.json")

This function ensures the dataset contains only numerical data. If non-numeric data is detected, an error is raised.

Checking Data Issues
--------------------

Use `datalizer.cleaner.check_for_issues` to inspect a dataset for missing values and duplicates:

.. code-block:: python

    import datalizer.cleaner as dc

    # Check for issues in the dataset
    dc.check_for_issues(df)

If missing or duplicate values exist, the function prints the details.

Cleaning Data
------------------------------------------------------------------------------------------------

Use `datalizer.cleaner.clean_basic` to clean a dataset by removing duplicates and handling missing values:

.. code-block:: python

    import datalizer.cleaner as dc

    # Clean missing values using the mean strategy
    cleaned_df = dc.clean_basic(df, strategy="mean")

    # Drop rows with missing values
    cleaned_df = dc.clean_basic(df, strategy="drop")

You can choose from `"mean"`, `"median"`, `"mode"`, or `"drop"` strategies.

Decorator for Numeric Validation
------------------------------------------------------------------------------------------------

Use `datalizer.utils.requires_numeric_data` to enforce numeric-only DataFrames in functions:

.. code-block:: python

    import pandas as pd
    from datalizer.utils import requires_numeric_data

    @requires_numeric_data
    def compute_average(df: pd.DataFrame) -> pd.Series:
        return df.mean()

The decorator raises an error if non-numeric data is found.

This usage guide provides a structured way to work with your modules. Let me know if you'd like any refinements!
