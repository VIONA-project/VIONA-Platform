"""Sphinx configuration for the VIONA documentation."""

from datetime import date

project = "VIONA"
author = "VIONA contributors"
copyright = f"{date.today().year}, VIONA contributors"
release = "development"
language = "en"

extensions = ["myst_parser", "sphinx.ext.githubpages"]
source_suffix = {".md": "markdown"}
root_doc = "index"
exclude_patterns = ["_build", "requirements.txt", "Thumbs.db", ".DS_Store"]
myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 3

html_theme = "sphinx_rtd_theme"
html_title = "VIONA Documentation"
html_short_title = "VIONA"
html_static_path = ["_static"]
html_css_files = ["viona.css"]
html_baseurl = "https://viona-project.github.io/VIONA-Platform/"
html_theme_options = {
    "style_nav_header_background": "#155e75",
    "collapse_navigation": False,
    "navigation_depth": 3,
    "sticky_navigation": True,
    "prev_next_buttons_location": "bottom",
}
html_context = {
    "display_github": True,
    "github_user": "VIONA-project",
    "github_repo": "VIONA-Platform",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
html_show_sourcelink = True
html_show_sphinx = False
