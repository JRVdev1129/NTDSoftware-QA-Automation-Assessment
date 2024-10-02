# Python Selenium

### Test Coverage

- [Google Search Tests](./specs/search/google_test.py)
  - Test type: E2E

### Local setup instructions

[Download and Install Python and pip package manager](https://www.python.org/)

#### Linux:

I Used Debian so if you are using any other distro you may need to change some of the code below accordingly.
* Install Python env `sudo apt install python3-venv`
* Create a Python environment `python3 -m venv .venv`
* Activate the Python environment you just created `source .venv/bin/activate`
* Install the necessary packages `pip install -r requirements.txt`

#### Windows:

[Instructions on how to install python virtual environment in case the instructions in this documentation are not enough](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)

* Install Python env `pip install virtualenv`
* Create a Python environment `python3 -m venv .venv`
* Activate the Python environment you just created `source .venv/bin/activate`
* Install the necessary packages `pip install -r requirements.txt`

### How to run tests locally

You can either Run the test using behave, pytest or pytest-bdd

Pytest-bdd(recommended):

* Run `pytest -s --count=1`

Behave:

* Run `behave`

Pytest:

Running the test with basic pytest only if you want to debug
to do this you will need to comment and uncomment some lines in [Google Search Tests](./specs/search/google_test.py)

* uncomment Line 1
* comment from line 6 to line 36
* uncomment from line 38 to line 69

* Run `pytest -s --count=1`

That should be enough to run the project

pd: this may change as more test are added
