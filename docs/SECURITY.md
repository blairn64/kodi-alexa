# Security Notes

This project controls a media system through a network API. Treat the deployment as a privileged integration point within a private network.

## Do not commit

- Kodi usernames or passwords
- Alexa application identifiers
- AWS access keys or secret keys
- Private certificates or private keys
- Publicly reachable personal IP addresses or DNS names
- Home-network topology or other private infrastructure details

## Recommended practice

Use environment variables or a secret manager for credentials. Restrict the Kodi API to trusted networks, prefer HTTPS where supported by the deployment, and avoid exposing the management interface directly to the public internet.

The example configuration files are templates only.
