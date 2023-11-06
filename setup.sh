#!/bin/bash

# Ensure the script fails if any command fails
set -e

# Check for Homebrew, install if we don't have it
if test ! $(which brew); then
  echo "Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Configure PATH for Homebrew on ARM Macs
echo "Configuring PATH for Homebrew..."
export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"

# Install Python 3 using Homebrew
echo "Installing Python..."
brew install python3

# Upgrade pip to the latest version
echo "Upgrading pip..."
pip3 install --upgrade pip

# Install virtualenv to create an isolated Python environment
echo "Installing virtualenv..."
pip3 install virtualenv

# Create a virtual environment for the project using python3 -m venv
echo "Creating a virtual environment..."
python3 -m venv selenium_env
source selenium_env/bin/activate

# Install Selenium using pip
echo "Installing Selenium package..."
pip3 install selenium

# Install requests if needed for API testing
echo "Installing requests package..."
pip3 install requests

# Install ChromeDriver for Selenium
echo "Installing ChromeDriver..."
brew install --cask chromedriver

# Verify ChromeDriver installation
if [[ $(chromedriver --version) ]]; then
  echo "ChromeDriver installed successfully."
else
  echo "ChromeDriver installation failed."
  exit 1
fi

# Deactivate virtual environment (if used)
# deactivate

echo "Setup complete. You can now run Selenium scripts with Python."
