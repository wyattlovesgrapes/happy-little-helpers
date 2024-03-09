# happy-little-helpers

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  

**v0.0.1**  

#

happy_little_helpers is a python package that gives you some happy little utils including:


## flash_env

easy flash drive credential management for moving from system to system.

```
get_flash_path() - get the path to your credentials flash drive automatically 

read_env() - check you are retrieving the right credentials
```
## debugger

quickly turn debugging console prints on and off

```
debug_print() - replaces the print() function

enable_debug_mode() - global function to enable debugging

disable_debug_mode() - global function to disable debugging (this is the default behavior)

```


## project-structure
```
happy-little-helpers
├─ .gitignore
├─ README.md
├─ LICENSE
├─ pyproject.toml
├─ src/  
|   └─ happy_little_helpers/
│     ├─ __init__.py
│     ├─ debugger.py
│     └─ flash_env.py
└─ tests/
   ├─ __init__.py
   ├─ credentials/
   │  └─ happy-little-helpers/
   │     └─ .env
   ├─ main_test.py
   └─ pythonpath.txt

```

## how to test locally

1. navigate to the root package directory `happy-little-helpers` and add the temp `PYTHONPATH` found in `happy-little-helpers/tests/pythonpath.txt`: 

```

export PYTHONPATH=/home/<username>>/Documents/github/happy-little-helpers/happy_little_helpers:$PYTHONPATH

```

2. format a flash drive and name the partition `credentials`. 

3. copy the contents of the `credentials` directory to your newly formated drive.

4. run `python3 tests/main_test.py` from your root directory to print the demo .env retrieved from your credentials flash drive.

