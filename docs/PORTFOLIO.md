# Portfolio Notes

## What this project shows

This project is useful evidence of hands-on Python application development and integration work. The interesting parts are the boundaries between systems rather than the voice interface itself.

### Integration
- Alexa intent handling feeds a Python application.
- The application calls Kodi through JSON-RPC.
- The same application can be adapted to Lambda, WSGI/Gunicorn or Docker-based deployment.

### Engineering themes
- API integration and request/response handling
- Runtime configuration through environment variables
- Separation of application logic from deployment concerns
- Automated generation of Alexa custom-slot data
- Logging and operational configuration

## What I would improve today

The codebase predates current Python packaging and deployment practices. A modern refresh would introduce a supported Python version, dependency pinning/locking, automated tests, typed interfaces for external API calls, structured logging, and a current deployment path.

The repository is therefore presented as a mature personal project and a record of engineering experience, not as a currently maintained commercial service.

## Security

Only connect the application to systems you own or are explicitly authorised to control. Keep credentials, private endpoints and household network information out of source control.
