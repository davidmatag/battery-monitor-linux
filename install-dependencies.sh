#!/bin/sh

if [ `id -u` -ne 0 ]
then
  echo "Please start this script with root privileges!"
  echo "Try again with sudo."
  exit 0
fi

echo "This script will install Battery Monitor"
echo "Do you wish to continue? (y/n)"

while true; do
  read -p "" yn
  case $yn in
      [Yy]* ) break;;
      [Nn]* ) exit 0;;
      * ) echo "Please answer with Yes or No [y|n].";;
  esac
done
echo ""
echo "============================================================"
echo ""
echo "Installing necessary dependencies... (This could take a while)"
echo ""
echo "============================================================"

apt-get update
apt-get install -y python acpi pyqt4-dev-tools
echo "============================================================"

if [ "$?" = "1" ]
then
  echo "An unexpected error occured during apt-get!"
  exit 0
fi
