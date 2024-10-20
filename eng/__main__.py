"""
CLI commands for the package.
"""

from eng.generate import generate_html
from eng.generate import generate_mjml

with open("index.html", "w") as f:
    f.write(generate_html(generate_mjml()))
