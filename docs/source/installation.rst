Installation
================================================================================================

Prerequisites
------------------------------------------------------------------------------------------------

Before installing Datalizer, ensure you have:

* Python 3.8 or newer
* pip (Python package manager)

Basic Installation
------------------------------------------------------------------------------------------------

You can install Datalizer using pip:

.. code-block:: bash

    pip install datalizer


Then you can use the package in your projects:


    import datalizer

Development Installation
------------------------------------------------------------------------------------------------

To install Datalizer for development:

1. Clone the repository:

   .. code-block:: bash

       git clone https://github.com/eorsjr/datalizer-scipy
       cd datalizer-scipy

2. Create a virtual environment:

   .. code-block:: bash

       python -m venv .venv
       source .venv/Scripts/activate  # On Windows with Git Bash
       # Or on Windows CMD: .\.venv\Scripts\activate.bat
       # Or on PowerShell: .\.venv\Scripts\Activate.ps1
       # Or on Linux/Mac: source .venv/bin/activate

3. Install development dependencies:

   .. code-block:: bash

       pip install -e ".[dev]"

       
============================================================================================================

To install the core package dependencies, run:

.. code-block:: bash

   pip install -r requirements.txt

To install documentation dependencies:

.. code-block:: bash

   pip install -r docs/requirements.txt
