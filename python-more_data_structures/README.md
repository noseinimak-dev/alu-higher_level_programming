cat > README.md << 'EOF'
# Python - More Data Structures

This directory contains tasks from the alu-higher_level_programming project on more advanced list and matrix operations in Python.

## Requirements

- Python 3 (tested on Ubuntu)
- All files start with `#!/usr/bin/python3`
- Code follows the pycodestyle style
- All files are executable
- No modules are imported unless a task allows it

## Files

| File | Description |
|------|-------------|
| `0-square_matrix_simple.py` | Function that returns a new matrix with the square of every integer in the given matrix, without modifying the original |

## Example

    $ cat 0-main.py
    #!/usr/bin/python3
    square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)

    $ ./0-main.py
    [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## Author

Nyamesomfo Ama osei-Nimako
EOF
