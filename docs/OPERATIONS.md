# Operations Notes

## Local development

1. Copy the environment template to a local, ignored environment file.
2. Provide the Kodi endpoint and application credentials through environment variables.
3. Install Python dependencies from the project requirements.
4. Run the web/handler entry point appropriate to the deployment mode.

## Deployment modes

### AWS Lambda

Package only the Lambda-relevant application files and dependencies. Keep AWS credentials out of the repository and use the execution role/CI environment for deployment authentication.

### Docker

Build the image from the supplied Dockerfile and inject runtime configuration at container start.

### WSGI

Run the application behind a suitable reverse proxy and use Gunicorn or another supported WSGI server.

## Troubleshooting checklist

- Verify the Kodi API endpoint is reachable from the runtime environment.
- Verify authentication values are present in the process environment.
- Check application logs for API or intent-handling errors.
- Confirm the Alexa interaction model matches the deployed intent and slot definitions.
- Avoid putting private network addresses or credentials into issues, screenshots or documentation.
