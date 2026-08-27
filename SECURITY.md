# Security Notes

This project uses configuration values for external services. Keep all credentials outside source control.

Never commit:
- Kodi usernames or passwords
- cloud access keys or secret keys
- Alexa skill secrets or application credentials
- private certificates or private keys
- personal addresses, hostnames or public tunnel credentials

Use environment variables or a local `.env` file that is excluded from Git. The checked-in environment template intentionally contains blank values.
