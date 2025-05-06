# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath("../../src"))  # Add the src path

project = 'Datalizer'
copyright = '2025, Eörs Szathmáry, Péter Osztobányi, Réka Kovács'
author = 'Eörs Szathmary, Péter Osztobanyi, Réka Kovács'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',  # For auto-generating docs from docstrings
              'sphinx.ext.napoleon',  # For supporting Google/NumPy style docstrings
              'nbsphinx',  # For including Jupyter notebooks
]

# nbsphinx_require_paths = {
#     'pandoc': False,
# }
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_context = {
"display_github": True,
"github_user": "eorsjr",
"github_repo": "datalizer-scipy",
'github_version': 'main',
'conf_py_path': '/docs/source/',
}