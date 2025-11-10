import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'email-multi-check'
copyright = 'email-multi-check Contributors'
author = 'email-multi-check Contributors'
version = "1.0"
release = '1.0.7'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [    
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
]

templates_path = ['_templates']

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store"
]

source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
#html_static_path = ['_static']

# The master toctree document.
master_doc = "index"

language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

autoclass_content = "both"

htmlhelp_basename = "email-multi-check_doc"

latex_elements = {}

latex_documents = [
    (master_doc, "email-multi-check.tex", "email-multi-check Documentation", "manual"),
]

texinfo_documents = [
    (
        master_doc,
        "email-multi-check",
        "email-multi-check Documentation",
        author,
        "email-multi-check",
        "One line description of project.",
        "Miscellaneous",
    ),
]

language = "en"