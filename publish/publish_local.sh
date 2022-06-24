#!/usr/bin/env bash
python3 -m venv venv
source venv/bin/activate
pip install wheel
cd publish
python setup.py sdist bdist_wheel && pip install dist/*.whl
python clean.py
