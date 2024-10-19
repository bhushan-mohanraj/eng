# Email Newsletter Generator Proposal

See https://github.com/TheStanfordDaily/email-newsletter-generator.

## Architecture

- MJML for email HTML (and the corresponding quirks)
    - A server or a process run by the Python package
- Jinja for templating

## Development

```bash
python -m black . # Format
python -m isort . --profile=black --sl # Sort imports
```

### Usage

```bash
python -m venv venv
source venv/Scripts/activate # Git Bash on Windows
python -m pip install -r requirements.txt
python -m eng ...
```

## TODO

- Pin dependencies from some `requirements.in`.
- Package with `pyproject.toml` if building a web server (not necessary).
