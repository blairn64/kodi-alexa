#!/usr/bin/env python3
"""Package the Lambda-specific files and run the legacy deployment command."""

from pathlib import Path
import shutil
import subprocess

APP_NAME = "kodi-alexa"
ROOT = Path.cwd()
TARGET = ROOT / APP_NAME

if TARGET.is_dir():
    shutil.rmtree(TARGET)

TARGET.mkdir()

for filename in (".env", "kodi.py", "wsgi.py", "requirements.txt"):
    source = ROOT / filename
    if source.is_file():
        shutil.copy2(source, TARGET / filename)

result = subprocess.run(
    ["lambda-deploy", "deploy"],
    cwd=TARGET,
    check=False,
    text=True,
    capture_output=True,
)

print(result.stdout, end="")
if result.stderr:
    print(result.stderr, end="")
raise SystemExit(result.returncode)
