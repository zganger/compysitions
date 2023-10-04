# Compysitions

![](https://github.com/zganger/extended_dataclass/workflows/Test/badge.svg)

## Project Overview
Python [dataclasses](https://docs.python.org/3/library/dataclasses.html "Dataclass documentation") are used to represent data in a python object.
They support decoding some data to dict out of the box, but do not handle all types neatly nor support loading to an instance from dict.
This project provides an extensible class that will allow you to define objects the way you would in a dataclass, 
but provides additional encoding and decoding support to represent these objects as data for i/o and storage purposes.

## Usage Examples
The below will show how Compysitions handles support for increasingly complex data describing transactions in a store.

### Built-in types
```python
class Transaction(Compysition):
    buyer_name: str = None
    item_name: str = None
    price: float = 0.00

transaction_data = {
    "buyer_name": "John Smith",
    "item_name": "Floral Shirt",
    "price": 20.99
}

transaction_obj = Transaction().from_dict(transaction_data)
```

## Setting up the development environment
The following steps will set up linting on commit and the ability to run tests.
1. Clone repository
2. Create a virtual environment for development
3. `pip install -r dev_requirements.txt`
4. `pre-commit install`
