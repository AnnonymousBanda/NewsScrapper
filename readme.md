# Project Setup and Development Guide

## Prerequisites

Make sure you have the following tools installed:

- **Python** (version 3.7 or higher)

## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AnnonymousBanda/NewsScrapper
   cd NewsScrapper
   code .
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Starting the Development Server

The project uses a script to auto-restart the Flask server when code changes are detected.

 Run the development script:
   ```bash
   scripts/dev.bat
   ```

This script uses the following command under the hood:
```bash
watchmedo auto-restart --pattern="*.py" --recursive -- flask run --host=0.0.0.0
```

## Notes

- Make sure to keep your virtual environment activated while working on the project.
- If you encounter any issues, ensure that all required dependencies are installed properly using:
  ```bash
  pip install -r requirements.txt
  ```
- Modify the `requirements.txt` file by running the following command after adding new dependencies:
  ```bash
  pip freeze > requirements.txt
  ```
