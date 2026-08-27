# Kodi Alexa Integration — Archived Legacy Project

A historical personal Python project connecting Amazon Alexa voice commands to Kodi through Kodi's JSON-RPC interface.

> **Archive:** this project is retained as a record of earlier development work. It is not presented as a current commercial service or as evidence of current cloud architecture.

## What it demonstrates

- Python application development
- JSON-RPC / HTTP API integration
- Voice intent handling
- AWS Lambda deployment patterns
- Docker and WSGI/Gunicorn deployment
- Environment-based configuration
- Application logging and operational configuration

## Architecture

```text
Alexa skill
    |
    v
Python handler / application
    |
    +---- Lambda deployment
    +---- WSGI / Gunicorn
    +---- Docker
    |
    v
Kodi JSON-RPC API
```

See `docs/ARCHITECTURE.md` and `docs/OPERATIONS.md` for the technical record.

## Configuration

Runtime configuration uses environment variables. Never commit credentials, tokens, certificates, private endpoints or local-network details.

## Portfolio position

This repository is intentionally kept secondary to the current infrastructure and automation portfolio. It is useful as evidence of having built and integrated a non-trivial personal application, but the technology is now legacy.
