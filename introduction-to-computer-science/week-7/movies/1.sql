/*  SQL query to list the titles of all movies released in 2008. */
SELECT
  movies.title
FROM
  movies
WHERE
  movies.year = 2008;