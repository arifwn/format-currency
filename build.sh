#!/usr/bin/env bash

set -euxo pipefail

echo "installing dependencies..."
python -m pip install --upgrade pip build hatch

echo "done!"