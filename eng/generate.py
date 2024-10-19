"""
Generate MJML for newsletters
and convert that MJML to HTML for an email.
"""

import pathlib

import jinja2

from eng.config import THE_DAILY_BASE_CONFIG
from eng.config import THE_DAILY_BASE_DESIGN_CONFIG

PACKAGE_NAME = "eng"


def generate_mjml() -> str:
    """
    Generate MJML for a newsletter.
    """


def generate_html(mjml: str) -> str:
    """
    Generate HTML from MJML source for a newsletter.
    This function expects that MJML has been installed as required.
    """
