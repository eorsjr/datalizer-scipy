Contributing
================================================================================================

Thank you for your interest in contributing to Datalizer! This document provides guidelines and instructions for contributing to this project.

Development Setup
------------------------------------------------------------------------------------------------

1. Fork the repository on GitHub
2. Clone your fork locally:

   .. code-block:: bash

       git clone https://github.com/eorsjr/datalizer-scipy
       cd datalizer-scipy

3. Create a virtual environment and install development dependencies:

   .. code-block:: bash

       # Create virtual environment
       python -m venv .venv
       
       # Activate the environment (Windows/Git Bash)
       source .venv/Scripts/activate
       
       # Or on macOS/Linux
       # source .venv/bin/activate
       
       # Install the package in development mode
       pip install -e ".[dev]"

4. Create a branch for your changes:

   .. code-block:: bash

       git checkout -b feature-or-bugfix-name

Code Style
------------------------------------------------------------------------------------------------

We follow PEP 8 style guidelines for Python code. Please ensure your code adheres to these standards.

Before submitting your changes, run:

.. code-block:: bash

    # Check code style
    flake8 datalizer
    
    # Run type checking
    mypy datalizer

Testing
------------------------------------------------------------------------------------------------

We use pytest for testing. Please write tests for any new functionality:

.. code-block:: bash

    # Run tests
    pytest
    
    # Run tests with coverage
    pytest --cov=datalizer

All tests should pass before submitting a pull request.

Documentation
------------------------------------------------------------------------------------------------

Documentation is written in reStructuredText (RST) and built using Sphinx:

1. Update docstrings for any new or modified functions
2. For significant changes, update or add appropriate documentation in the ``docs/`` directory
3. Build the documentation to verify your changes:

   .. code-block:: bash

       cd docs
       make html
       # View the docs in your browser by opening build/html/index.html

Pull Request Process
------------------------------------------------------------------------------------------------

1. Update the documentation with details of changes as needed
2. Ensure all tests pass
3. Update the version number in ``setup.py`` following semantic versioning
4. Submit a pull request to the main repository

Guidelines for Pull Requests:

- Keep pull requests focused on a single feature or bug fix
- Include tests for new functionality
- Provide a clear description of the changes
- Reference any related issues

Code Review
------------------------------------------------------------------------------------------------

All submissions require review. We use GitHub pull requests for this purpose:

1. Submit your pull request
2. Address any feedback or requested changes
3. Once approved, a maintainer will merge your changes

Issue Reporting
------------------------------------------------------------------------------------------------

If you find a bug or have a suggestion for improvement:

1. Check existing issues to see if it has already been reported
2. If not, create a new issue with:
   - A clear title and description
   - Steps to reproduce the issue
   - Expected and actual behavior
   - Any relevant code snippets or error messages

Feature Requests
------------------------------------------------------------------------------------------------

Feature requests are welcome! Please provide:

- A clear description of the feature
- The use case or problem it addresses
- Any ideas for implementation

License
------------------------------------------------------------------------------------------------

By contributing to Datalizer, you agree that your contributions will be licensed under the same license as the project.

Thank You
------------------------------------------------------------------------------------------------

Your contributions help make Datalizer better for everyone. We appreciate your time and effort!