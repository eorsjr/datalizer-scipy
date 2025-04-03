Cleaner
================================================================================================



Checking Data Issues
-------------------------------------------------------------------------------------------------

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



This usage guide provides a structured way to work with your modules. Let me know if you'd like any refinements!
