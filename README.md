# Kodi Alexa Integration

A Python service that connects Amazon Alexa voice commands to Kodi through Kodi's JSON-RPC interface.

## What it demonstrates

- Python application development
- JSON-RPC / HTTP API integration
- Voice intent handling
- AWS Lambda deployment
- Docker-based deployment
- WSGI/Gunicorn deployment
- Environment-based configuration
- Automated Alexa custom-slot generation
- Application logging and operational configuration

## Capabilities

The application supports voice-driven Kodi navigation, playback control, volume adjustment, media search, playlists, random media selection, TV episode selection, library maintenance and selected system controls.

## Architecture

```text
Alexa skill
    |
    v
Python application / handler
    |
    +---- AWS Lambda deployment
    +---- WSGI / Gunicorn deployment
    +---- Docker deployment
    |
    v
Kodi JSON-RPC API
    |
    v
Media library / playback
```

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the component model and [`docs/OPERATIONS.md`](docs/OPERATIONS.md) for deployment and troubleshooting notes.

## Configuration

Runtime configuration is supplied through environment variables. Typical values are:

```text
KODI_ADDRESS=<your-kodi-host>
KODI_PORT=<your-kodi-port>
KODI_USERNAME=<your-kodi-user>
KODI_PASSWORD=<your-kodi-password>
SKILL_APPID=<your-alexa-app-id>
```

Never commit real credentials, tokens, certificates or private endpoints. See [`SECURITY.md`](SECURITY.md).

## Repository layout

- `kodi.py` — core application and Kodi integration logic
- `wsgi.py` — WSGI entry point
- `deploy-to-lambda.py` — Lambda packaging/deployment helper
- `generate_custom_slots.py` — Alexa slot generation utility
- `alexa.intents` — voice intents
- `alexa.utterances` — voice training utterances
- `Dockerfile` — container deployment
- `gunicorn.conf` — WSGI process configuration
- `logging.conf` — logging configuration
- `docs/` — architecture and operational documentation

## Project status

A mature personal project retained as an example of Python integration, API consumption, voice-interface design and cloud/container deployment. It is not presented as a current commercial service.

## Safety

Use only with systems you own or are explicitly authorised to control. Keep local network details, credentials and private media-library information out of Git.
