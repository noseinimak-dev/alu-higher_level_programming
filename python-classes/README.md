# python-classes

This directory contains Python scripts that introduce classes and objects: defining a class, private instance attributes, validating values, getters and setters (properties), and instance methods.

## Requirements

- Python 3 (interpreter `/usr/bin/python3`)
- All files start with `#!/usr/bin/python3`
- All files are executable
- No modules are imported
- Code follows the `pycodestyle` style
- All classes and methods are documented with docstrings

## Files

| File | Description |
|------|-------------|
| `1-square.py` | `Square` class with a private instance attribute `size` (no validation) |
| `2-square.py` | Adds optional `size` (default `0`) with type and value validation |
| `3-square.py` | Adds the public instance method `area()` |
| `4-square.py` | Adds a property getter and setter for `size` |
| `5-square.py` | Adds the public instance method `my_print()` that prints the square with `#` |
| `6-square.py` | Adds a private `position` attribute (getter and setter) used by `my_print()` |

## Error messages

- `size must be an integer` (`TypeError`)
- `size must be >= 0` (`ValueError`)
- `position must be a tuple of 2 positive integers` (`TypeError`)

## Author

ALU Higher Level Programming student
