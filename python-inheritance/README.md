# Python - Inheritance

This directory is part of the `alu-higher_level_programming` repository. It covers class inheritance in Python, including `dir()`, `isinstance()`, `issubclass()`, subclassing built-in types, and building classes on top of other classes.

## Requirements

- Python 3 (all files start with `#!/usr/bin/python3`)
- Code follows the `pycodestyle` style
- All modules, classes, and functions have documentation
- All files end with a new line
- All files are executable

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Function that returns the list of available attributes and methods of an object |
| `1-my_list.py` | Class `MyList` that inherits from `list` and adds a method to print the list sorted in ascending order |
| `2-is_same_class.py` | Function that returns `True` if an object is exactly an instance of the specified class |
| `3-is_kind_of_class.py` | Function that returns `True` if an object is an instance of, or inherited from, the specified class |
| `4-inherits_from.py` | Function that returns `True` if an object is an instance of a class that inherited (directly or indirectly) from the specified class |
| `5-base_geometry.py` | Empty class `BaseGeometry` |
| `6-base_geometry.py` | `BaseGeometry` with a public instance method `area()` that raises an `Exception` |
| `7-base_geometry.py` | `BaseGeometry` with a public instance method `integer_validator(name, value)` |
| `8-rectangle.py` | Class `Rectangle` that inherits from `BaseGeometry` |
| `9-rectangle.py` | `Rectangle` with `area()` and a custom `__str__` |
| `10-square.py` | Class `Square` that inherits from `Rectangle` |
| `11-square.py` | `Square` with a custom `__str__` |
| `tests/1-my_list.txt` | Doctest file for `1-my_list.py` |
| `tests/7-base_geometry.txt` | Doctest file for `7-base_geometry.py` |

## Usage

Run a task with its main file, for example:

```bash
./0-main.py
```

Run the doctests with:

```bash
python3 -m doctest -v ./tests/1-my_list.txt
python3 -m doctest -v ./tests/7-base_geometry.txt
```

## Author

noseinimak-dev
