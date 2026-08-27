# Kodi Alexa Integration

A Python service that connects Amazon Alexa voice commands to Kodi over Kodi's JSON-RPC interface.

## What it demonstrates

- Python application development
- REST/JSON-RPC integration
- Voice intent handling
- AWS Lambda deployment
- Containerised deployment with Docker
- WSGI/Gunicorn deployment
- Environment-based configuration
- Automated generation of Alexa custom slots
- Application logging and operational configuration

## Capabilities

The project supports voice-driven Kodi navigation, playback control, volume adjustment, media search, playlists, random media selection, TV episode selection, library maintenance and system controls.

## Architecture

```text
Alexa
  |
  v
Application / Lambda handler
  |
  v
Python service
  |
  v
Kodi JSON-RPC API
```

The project can be deployed as an AWS Lambda-based service, a container, or a traditional WSGI application depending on the environment.

## Configuration

Configuration is supplied through environment variables. The repository does not require real credentials in source control.

Typical values include:

```text
KODI_ADDRESS=<your-kodi-host>
KODI_PORT=<your-kodi-port>
KODI_USERNAME=<your-kodi-user>
KODI_PASSWORD=<your-kodi-password>
SKILL_APPID=<your-alexa-app-id>
```

Never commit real credentials, tokens, certificates or private endpoints.

## Repository layout

- `kodi.py` — core application logic
- `deploy-to-lambda.py` — Lambda deployment helper
- `generate_custom_slots.py` — Alexa slot generation utility
- `alexa.intents` — voice intent definitions
- `alexa.utterances` — voice utterance training data
- `Dockerfile` — container deployment
- `gunicorn.conf` — WSGI process configuration
- `logging.conf` — logging configuration

## Project status

This is a mature personal project with a large existing codebase. It is retained as an example of Python integration work and cloud deployment rather than as a current commercial service.

## Safety

Use only with systems you own or are explicitly authorised to control. The repository should contain configuration templates and placeholders rather than real household network details or credentials.
