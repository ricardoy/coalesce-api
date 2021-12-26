# Installation 

```shell
conda create --name nirvana python=3.9
conda activate nirvana

 
pip install pip-tools pip-compile-multi

# pip-compile will generate the requirements.txt file based on requirements.in
pip-compile

pip install -r requirements.txt
```


# Running the example


1. Open a terminal with the configured Python environment and run:
```shell
python dummy_server.py 
```

2. Open another terminal with the configured Python environment and run:
```shell
python main.py --config config.ini
```


# Mypy

To run mypy static analysis:

```shell
mypy .
```

Observation: `dummy_server.py` is ignored because I was having trouble setting the Flask types correctly.


