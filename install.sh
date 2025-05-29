#!/bin/bash

echo "📦 Installing required packages for IP Info Tool..."

# Update package list
pkg update -y && pkg upgrade -y

# Install Python and pip if not already installed
pkg install -y python

# Install required Python modules
pip install --upgrade pip
pip install requests colorama prettytable


echo ""
echo "✅ All required packages have been installed!"
echo "🚀 You can now run your IP Info Tool using: python your_script.>

# clear
 clear
# run
  python ip_track.py
