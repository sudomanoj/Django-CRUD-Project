# Django-CRUD-Project
Django Code to perform Create Read and Delete operation

# GoCardless sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/onlymanoj/Django-CRUD-Project.git
$ cd Django-CRUD-Project/
$ pip3 install -r requirements. txt
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

In order to test the working flows, fill in the form details in
`http://127.0.0.1:8000/` to match your **SANDBOX** developer credentials.

## Walkthrough

You can insert Data, Update them and modify them


