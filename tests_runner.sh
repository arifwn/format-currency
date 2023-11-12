#!/usr/bin/env bash

set -euxo pipefail

# python -m unittest discover
hatch run test

echo "done!"