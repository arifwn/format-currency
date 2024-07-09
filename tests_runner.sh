#!/usr/bin/env bash

set -euxo pipefail

# python -m unittest discover
hatch test -py 3.7
hatch test -py 3.8
hatch test -py 3.9
hatch test -py 3.10
hatch test -py 3.11
hatch test -py 3.12

echo "done!"