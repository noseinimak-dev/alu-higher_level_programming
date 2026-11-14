# python-more_classes

This directory contains Python scripts that go further with classes and objects: properties, class attributes, static and class methods, and the special methods `__str__`, `__repr__` and `__del__`.

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
| `0-rectangle.py` | Empty `Rectangle` class |
| `1-rectangle.py` | Private `width` and `height` with getters, setters and validation |
| `2-rectangle.py` | Adds `area()` and `perimeter()` |
| `3-rectangle.py` | Adds `__str__` to print the rectangle with `#` |
| `4-rectangle.py` | Adds `__repr__` so `eval(repr(rect))` recreates the rectangle |
| `5-rectangle.py` | Prints `Bye rectangle...` when an instance is deleted |
| `6-rectangle.py` | Adds the class attribute `number_of_instances` |
| `7-rectangle.py` | Adds the class attribute `print_symbol` used by `__str__` |
| `8-rectangle.py` | Adds the static method `bigger_or_equal(rect_1, rect_2)` |
| `9-rectangle.py` | Adds the class method `square(size=0)` |

## Error messages

- `width must be an integer` (`TypeError`)
- `width must be >= 0` (`ValueError`)
- `height must be an integer` (`TypeError`)
- `height must be >= 0` (`ValueError`)
- `rect_1 must be an instance of Rectangle` (`TypeError`)
- `rect_2 must be an instance of Rectangle` (`TypeError`)

## Author

ALU Higher Level Programming student
