#!/bin/bash
python3 -m venv venv-cicdvenom
source venv-cicdvenom/bin/activate
pip install . --force-reinstall
echo 'Run: source venv-cicdvenom/bin/activate && cicdvenom --target /path --interactive'