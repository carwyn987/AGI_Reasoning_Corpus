#!/bin/bash

# Set up venv (if doesn't exist) and source

source common_scripts/setup_env.sh

export ARC_AGI_BASE=$BASE_DIR/ARC-AGI
export RAVEN_BASE=$BASE_DIR/RAVEN
export BONGARD_LOGO_BASE=$BASE_DIR/BONGARD_LOGO

if [ ! -d "$BONGARD_LOGO_BASE/bongard_logo_dataset" ]; then
  echo "$BONGARD_LOGO_BASE/bongard_logo_dataset not found, removing any artifacts of .tgz, and running populate script..."
  rm $BONGARD_LOGO_BASE/bongard_logo_dataset.tgz
  "$BASE_DIR/src/populate_bongard_logo.sh"
fi


# Deactivate venv

# Cleanup