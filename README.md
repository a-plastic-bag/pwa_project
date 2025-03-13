# PWA Project
This is the GitHub repository for my second HSC SEN Assessment.

## Setup

### Prerequisites:
* Python 3.13.12

### Steps:
1. Clone this repository and `cd` into it.
2. Run the following: `python3 -m venv .env` to create a virtual environment.
3. Activate the virtual environment:
  - If using windows, run `.\.env\bin\Activate.ps1`
  - If using Bash, run `source .env/bin/activate`
  - If using C shell, run `source .env/bin/activate.csh`
  - If using Fish, run `source .env/bin/activate.fish`
4. Run `pip3 install -r requirements.txt` to install dependencies
5. Run `python3 manage.py makemigrations` and `python3 manage.py migrate` to create Django migrations
6. Run the server with `python3 manage.py runserver`
7. Run `deactivate` to exit the virtual environment when done.
