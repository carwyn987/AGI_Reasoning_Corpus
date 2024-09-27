#!/bin/bash

################ Dowload and extract dataset #######################

bongard_logo_download_link='https://drive.usercontent.google.com/download?id=1-1j7EBriRpxI-xIVqE6UEXt-SzoWvwLx&export=download&authuser=1&confirm=t'
wget $bongard_logo_download_link -O $BASE_DIR/BONGARD_LOGO/bongard_logo_dataset.tgz

echo "Extracting tarball..."
unzip "$BASE_DIR/BONGARD_LOGO/bongard_logo_dataset.tgz" -d "$BASE_DIR/BONGARD_LOGO/bongard_logo_dataset"
TAR_EXIT_STATUS=$?

if [ $TAR_EXIT_STATUS -ne 0 ]; then
  echo "Error extracting tarball: $TAR_EXIT_STATUS"
  exit 1
fi


echo "Removing compressed file..."
rm "$BASE_DIR/BONGARD_LOGO/bongard_logo_dataset.tgz"

################# Set up virtual environment ########################
