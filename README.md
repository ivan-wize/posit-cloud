# Selenium Automation Script for posit.cloud

This repository contains a Selenium automation script for logging in, creating, and deleting a space in the posit.cloud application.

## Prerequisites

Before you execute the script, make sure you have the following installed:

- Python 3
- Homebrew (for macOS)
- Git (optional, to clone the repository)

## Setup

To set up your environment to run the Selenium script, follow these steps:

1. Clone the repository (optional):

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Run the setup script:

    ```sh
    ./setup.sh
    ```

    This script will:

    - Install Homebrew (if it's not already installed).
    - Install Python3 via Homebrew.
    - Upgrade pip to the latest version.
    - Install virtualenv and create a virtual environment.
    - Install Selenium and requests packages.
    - Install ChromeDriver.

## Running the Script

After setting up your environment, you can run the `testrun.py` script as follows:

1. Ensure your virtual environment is activated:

    ```sh
    source selenium_env/bin/activate
    ```

2. Run the script:

    ```sh
    python3 testrun.py
    ```

The script will perform the following actions:

- Open the login page of posit.cloud.
- Log in using hardcoded credentials (test user).
- Create a new space named "Test Space".
- Delete the newly created space.

**Note:** The script uses hardcoded `time.sleep()` calls for simplicity, which are not best practice for production code but can be modified further in the process

## Cleanup

After you're done running the script, you can deactivate the virtual environment:

```sh
deactivate
