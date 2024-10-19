"""
Generate MJML for newsletters
and convert that MJML to HTML for an email.
"""

import datetime
import pathlib

import jinja2

from eng.config import THE_DAILY_BASE_CONFIG
from eng.config import THE_DAILY_BASE_DESIGN_CONFIG

PACKAGE_NAME = "eng"
NEWSLETTER_TEMPLATE_LOCATION = "newsletter.mjml.jinja"


def generate_mjml() -> str:
    """
    Generate MJML for a newsletter.
    """

    template_environment = jinja2.Environment(
        loader=jinja2.PackageLoader(PACKAGE_NAME),
        autoescape=jinja2.select_autoescape(),
    )

    template = template_environment.get_template(NEWSLETTER_TEMPLATE_LOCATION)

    return template.render(
        {
            "datetime": datetime,
            "base_config": THE_DAILY_BASE_CONFIG,
            "base_design_config": THE_DAILY_BASE_DESIGN_CONFIG,
        }
    )


def generate_html(mjml: str) -> str:
    """
    Generate HTML from MJML source for a newsletter.
    This function expects that MJML has been installed as required.
    """
