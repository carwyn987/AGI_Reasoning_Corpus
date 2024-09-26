#!/bin/bash


# SET BASE DIRECTORY, both if sourced and if executed
if [ -n "$BASH_SOURCE" ]; then
  export BASE_DIR=$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")
else
  export BASE_DIR=$(dirname "$(dirname "$(readlink -f "$0")")")
fi

