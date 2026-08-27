# Architecture

## Overview

The application bridges voice intents from Amazon Alexa to Kodi's JSON-RPC API.

```text
Alexa skill
    |
    v
Python web/handler layer
    |
    +---- AWS Lambda deployment option
    |
    +---- WSGI/Gunicorn deployment option
    |
    +---- Docker deployment option
    |
    v
Kodi JSON-RPC API
    |
    v
Media library / playback system
```

## Components

### Python application

`kodi.py` contains the core command and Kodi API integration logic.

### Alexa definitions

`alexa.intents` and `alexa.utterances` define the voice interaction model. `generate_custom_slots.py` automates generation of custom slot data.

### Deployment

The project includes multiple deployment paths: AWS Lambda, a WSGI/Gunicorn service, and Docker. `deploy-to-lambda.py` supports the Lambda workflow.

### Configuration

Runtime settings are supplied through environment variables rather than source-controlled credentials. The repository's environment files are templates only.

## Engineering concerns

- Keep Kodi endpoints and credentials out of source control.
- Use HTTPS/reverse-proxy protection where appropriate for exposed deployments.
- Treat the Lambda deployment as an adapter around the application rather than mixing deployment secrets into application code.
- Keep logging useful but avoid recording credentials or private media-library information.
