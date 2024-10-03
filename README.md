# Learning Python and FastAPI

This project will document and contain my journey learning Python fundamentals and building RESTful API's using Python.

### Creating a Python virtual environment (venv):

A self contained location that enables you to maintain, separate, and isolate, environments for a python project.

e.g. rather installing dependencies globally, which could cause conflicts in other python projects, we can set up a venv that would allow us to manage the following locally:

- manage dependencies
- python interpreter versions
- third party packages and versions

To create a venv:

```
python3 -m venv [venv name]
```

> Note: venv's are not checked into source control systems such as Git.
> https://docs.python.org/3/library/venv.html

---

### Using a venv

Run `ls` to check for venv name

Activate the venv in a terminal:

```
source [...venv name]/bin/activate
```

To deactivate a venv run `deactivate` in the terminal.

---

### Deleting a venv

```
sudo rm -rf [venv name]
```

---

### Using the PIP package manager

Check globally installed packages:

```
python3 -m pip list
```

Check venv installed packages:

```
pip list
```

---

### Installing packages with PIP

Global installations:

```
python3 -m pip install "SomePackage[...]"
```

Local venv installations:

```
pip install "SomePackage[...]"
```

> Note: wrap package name around quotation marks

---

### Creating and using Project dependencies (requirements)

Saving requirements:

```
pip freeze > requirements.txt
```

Installing requirements:

```
pip install -r requirements.txt
```

Read requirements:

```
nano requirements.txt
```

---

### Dependencies used:

- Uvicorn - async web server implementation for Python.
- FastAPI - a modern, fast (high-performance), web framework for building APIs with Python.

---

### Sources:

- Python cheat sheet: https://www.pythoncheatsheet.org/
- https://packaging.python.org/en/latest/tutorials/installing-packages/
