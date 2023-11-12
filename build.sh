#!/usr/bin/env bash

set -euxo pipefail

echo "installing dependencies..."
python -m pip install --upgrade pip build hatch twine
python -m build
# python -m twine upload dist/*
python -m twine upload --repository testpypi dist/*

echo "done!"