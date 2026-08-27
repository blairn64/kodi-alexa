# Architecture

## Overview

The project bridges voice intents from Amazon Alexa to a Kodi media system through Kodi's JSON-RPC interface.

```text
Alexa skill
    |
    v
Python application / handler
    |
    +---- AWS Lambda deployment
    |
    +---- WSGI / Gunicorn deployment
    |
    +---- Docker deployment
    |
    v
Kodi JSON-RPC API
    |
    v
Media library and playback
```

## Components

- `kodi.py` contains the core command and Kodi API integration logic.
- `wsgi.py` supplies the web/WSGI entry point.
- `deploy-to-lambda.py` packages the Lambda deployment set.
- `generate_custom_slots.py` generates Alexa custom-slot data.
- `alexa.intents` and `alexa.utterances` define the interaction model.
- `Dockerfile` and `gunicorn.conf` describe alternative application runtimes.

## Configuration

Runtime settings are injected through environment variables. The repository's environment files are templates and should never contain real secrets, private endpoints or access credentials.

## Engineering concerns

- Keep Kodi endpoints and credentials out of source control.
- Use a protected reverse proxy and HTTPS when exposing the service beyond a trusted local network.
- Keep deployment credentials in AWS roles, CI/CD secrets or another approved secret store.
- Keep logging useful without recording credentials or private media-library information.

## Historical context

This is a personal integration project that demonstrates API integration, voice intent handling, cloud deployment and container/WSGI packaging. It is not presented as a current commercial service.
