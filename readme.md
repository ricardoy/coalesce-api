# Installation 

```shell
conda create --name nirvana python=3.9
conda activate nirvana

 
pip install pip-tools pip-compile-multi

# pip-compile-multi will generate the .txt files for the requirements/.in files
pip-compile-multi

pip install -r requirements/tests.txt
```


# Running the example


1. Open a terminal with the configured Python environment and run:
```shell
python dummy_server.py 
```

2. Open another terminal with the configured Python environment and run:
```shell
python main.py --config config.ini --coalesce-strategy avg

# or

python main.py --config config.ini --coalesce-strategy min
```


# Mypy

To run mypy static analysis:

```shell
mypy .
```

Observation: `dummy_server.py` is ignored because I was having trouble setting the Flask types correctly.


# Tests

1. Open a terminal with the configured Python environment and run:
```shell
pytest 
```
