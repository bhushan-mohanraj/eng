# Email Newsletter Generator Proposal

## Architecture

- MJML for email HTML (and the corresponding quirks)
    - A server or a process run by the Python package
- Jinja for templating

## Development

```bash
python -m venv venv
source venv/Scripts/activate # Git Bash on Windows
python -m pip install -r requirements.txt
python -m eng ...
```

## TODO

- Pin dependencies from some `requirements.in`.
- Package with `pyproject.toml` if building a web server (not necessary).
