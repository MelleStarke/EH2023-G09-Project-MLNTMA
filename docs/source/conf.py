# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ML-NTMA'
copyright = '2024, RUG'
author = 'Constantinos Kyriakides, Melle Starke, Aditya Menon'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_immaterial'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_css_files = ["docs/theme/custom.css",
                  "../theme/custom.css",
                  "./docs/theme/custom.css",
                  "./../theme/custom.css"]
html_theme = 'sphinx_immaterial'  # 'sphinx_rtd_theme'
html_theme_options = {
    "palette": { "scheme":  "slate",
                 "primary": "light-green",
                 "accent":  "lime" },
    "font": {"text": "Raleway",
             "code": "Roboto Mono"}
}

# -- Options for EPUB output
epub_show_urls = 'footnote'