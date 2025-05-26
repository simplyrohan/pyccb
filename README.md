# pyccb
Python Compiler Collection for Bash

## What is it
`pyccb` is a Python -> Pure Bash compiler. It can be used for anything, like making your bash scripts in a more familiar language or running your Python scripts in Bash for fun!

## How to use it
`pyccb` can be used as a CLI or as a Python package.

**Installation:**
```bash
# In the cloned repository
pip install -e .
```

**CLI Usage:**
```bash
pyccb -h
```
```bash
pyccb examples/helloworld.py -o helloworld.sh
```

**Python Package Usage:**
```py
import pyccb

pyccb.compile("print ('Hello World')")
```