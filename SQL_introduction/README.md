# SQL - Introduction

This directory is part of the `alu-higher_level_programming` repository. It covers the basics of SQL and MySQL: creating and deleting databases and tables, inserting, selecting, updating and deleting rows, and using aggregate functions.

## Requirements

- All files are interpreted on MySQL 8.0 (Ubuntu 20.04 LTS)
- All files end with a new line
- All files start with a comment describing the task
- SQL keywords are written in uppercase

## Files

| File | Description |
|------|-------------|
| `0-list_databases.sql` | Lists all databases of the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it does not exist |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all the tables of a database |
| `4-first_table.sql` | Creates the table `first_table` |
| `5-full_table.sql` | Prints the full description of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts a new row in `first_table` |
| `8-count_89.sql` | Displays the number of records with `id = 89` |
| `9-full_creation.sql` | Creates `second_table` and adds multiple rows |
| `10-top_score.sql` | Lists all records of `second_table` ordered by score (top first) |
| `11-best_score.sql` | Lists records with a score >= 10 |
| `12-no_cheating.sql` | Updates the score of Bob to 10 |
| `13-change_class.sql` | Removes all records with a score <= 5 |
| `14-average.sql` | Computes the score average |
| `15-groups.sql` | Lists the number of records with the same score |
| `16-no_link.sql` | Lists records that have a name, by descending score |

## Usage

Run a script with: cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

For scripts that use a database, pass its name as an argument: cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

## Author

noseinimak-dev
