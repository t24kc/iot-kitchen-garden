# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import toml

project_dir = os.path.abspath('../../')
sys.path.insert(0, project_dir)

# -- Project information -----------------------------------------------------

project = 'iot-kitchen-garden'
copyright = '2022, Takashi Suzuki'
author = 'Takashi Suzuki'

# The full version, including alpha/beta/rc tags
def get_version(project_dir: str) -> str:
    pyproject_path = f"{project_dir}/pyproject.toml"
    with open(pyproject_path) as f:
        pyproject_toml = toml.load(f)
        return pyproject_toml["tool"]["poetry"]["version"]


release = get_version(project_dir)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Other Options.
html_show_sourcelink = False
html_show_sphinx = False
autoclass_content = 'both'
