# SQL - More Queries

This directory is part of the `alu-higher_level_programming` repository. It covers MySQL users and privileges, table constraints (NOT NULL, DEFAULT, UNIQUE, PRIMARY KEY, FOREIGN KEY), subqueries, and JOINs.

## Requirements

- All files are interpreted on MySQL 8.0 (Ubuntu 20.04 LTS)
- All files end with a new line
- All files start with a comment describing the task
- SQL keywords are written in uppercase

## Files

| File | Description |
|------|-------------|
| `0-privileges.sql` | Lists all privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and `user_0d_2` with SELECT only |
| `3-force_name.sql` | Creates the table `force_name` where `name` cannot be null |
| `4-never_empty.sql` | Creates the table `id_not_null` with a default `id` of 1 |
| `5-unique_id.sql` | Creates the table `unique_id` with a unique `id` |
| `6-states.sql` | Creates the database `hbtn_0d_usa` and the table `states` |
| `7-cities.sql` | Creates the table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Lists the cities of California using a subquery |
| `9-cities_by_state_join.sql` | Lists all cities with their state name |
| `10-genre_id_by_show.sql` | Lists shows that have at least one genre linked |
| `11-genre_id_all_shows.sql` | Lists all shows, with NULL for shows without a genre |
| `12-no_genre.sql` | Lists shows without a genre linked |
| `13-count_shows_by_genre.sql` | Lists genres with the number of shows linked |
| `14-my_genres.sql` | Lists all genres of the show Dexter |
| `15-comedy_only.sql` | Lists all Comedy shows |
| `16-shows_by_genre.sql` | Lists all shows and their genres |

## Usage

Run a script with: cat 1-create_user.sql | mysql -hlocalhost -uroot -p

For scripts that use a database, pass its name as an argument: cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

Tasks 10 to 16 need the `hbtn_0d_tvshows` database dump imported first.

## Author

noseinimak-dev
