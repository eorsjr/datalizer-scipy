Loader
================================================================================================


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
