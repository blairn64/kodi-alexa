# Security and Privacy

This project is a personal integration and should only be deployed against systems you own or are explicitly authorised to control.

## Never commit

- Kodi usernames or passwords
- Alexa skill secrets or application credentials
- AWS access keys or deployment secrets
- private IP addresses or internal DNS names
- certificates or private keys
- private network configuration
- personal media-library data

## Configuration

Use environment variables or a local `.env` file that is excluded from Git. The checked-in environment template intentionally contains blank values.

## Before publishing changes

Review source, configuration, documentation and screenshots for private endpoints, credentials and personal information. Never paste private configuration into a public issue or pull request.
