# PythonMonkey - Playground
## Description
This is a playground for python library - PythonMonkey

## Installation

```bash
# Install all JS dependencies
$ yarn install
# Install all python libraries
$ poetry install
```

## Running the app
Just run corresponding python files.

## Personal thoughts
Found major inconveniences working with library, even trivial code:
1. No code completion when calling JS functions in python
2. Hard to debug. Before investigating the error, you first have to find where error is coming from. Extra layer of complexity.

Some interesting things:
1. It is possible to little bit "mixin" JS and Python code. E.g. provide python lambda for JS function which iterates over collection.

Verdict: Use it only when JS library has extremely high code coverage by test. And you have no alternatives amongst Python libraries.