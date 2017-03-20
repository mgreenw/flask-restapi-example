# flask-restapi-example
A simple RESTful API created using Flask and sqlalchemy that interacts with a PostgreSQL database of doctors and reviews

Software Versions Used:
Python 3.6.0

Installation:

1) Clone the Github repo: `$ git clone git@github.com:mgreenw/flask-restapi-example.git`
2) Move into the project directory `$ cd flask-restapi-example`
3) Setup a virtual environment in the project folder using python3: `$ python3 -m venv /path/to/project-parent-folder/flask-restapi-example/venv`
4) Start the virtual environment. You should see `(venv)` in as part of the command prompt once it is started: `$ source /path/to/project-parent-folder/flask-restapi-example/venv/bin/activate`
5) To stop the virtual environment at any time, run `(venv) $ deactivate`
6) Install all the requirements, including flask. Be sure not to use `sudo` as this will install flask in the global environment instead of the virtual environment: `(venv) $ pip3 install -r requirements.txt`
7) In a separate terminal window, install PostgreSQL. To do this, either install PostgreSQL.app or use HomeBrew for MacOS: `$ brew install postgresql`
8) If using Homebrew, start PostgreSQL: `$ postgres -D /usr/local/var/postgres`
9) In a separate terminal window, run `$ psql`. Then, run `# CREATE DATABASE doctor_reviews;`
10) Finally, run `# \q` to quit psql, and back in the original terminal window run `(venv) $ python3 setup.py` to initialize the database tables.

To Run:

1) Set an export path for flask: `(venv) $ export FLASK_APP=app.py`
2) Run flask! `(venv) $ flask run`
3) Go to http://127.0.0.1:5000 in a browser
