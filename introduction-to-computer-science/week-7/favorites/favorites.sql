UPDATE shows
SET
  title = "How I Met Your Mother"
WHERE
  title = "How i met your mother";

UPDATE shows
SET
  title = "Adventure Time"
WHERE
  title = "adventure time";

UPDATE shows
SET
  title = "Arrow"
WHERE
  title = "arrow";

UPDATE shows
SET
  title = "Avatar: The Last Airbender"
WHERE
  title LIKE "Avatar%";

UPDATE shows
SET
  title = "Brooklyn Nine-Nine"
WHERE
  title LIKE "Brooklyn%";

UPDATE shows
SET
  title = "Community"
WHERE
  title LIKE "Community%";

UPDATE shows
SET
  title = "Family Guy"
WHERE
  title LIKE "family%";

UPDATE shows
SET
  title = "Friends"
WHERE
  title LIKE "friends%";

UPDATE shows
SET
  title = "Billions"
WHERE
  title = "billions";

UPDATE shows
SET
  title = "Criminal Minds"
WHERE
  title = "criminal minds";

UPDATE shows
SET
  title = "Game of Thrones"
WHERE
  title LIKE "game of%";

UPDATE shows
SET
  title = "Gilmore Girls"
WHERE
  title LIKE "Gilmore girls";

UPDATE shows
SET
  title = "Grey’s Anatomy"
WHERE
  title LIKE "Grey%";

UPDATE shows
SET
  title = "It’s Always Sunny in Philadelphia"
WHERE
  title = "Its Always Sunny in Philidelphia";

UPDATE shows
SET
  title = "Parks and Recreation"
WHERE
  title LIKE "Parks and Rec%";

UPDATE shows
SET
  title = "Sherlock"
WHERE
  title LIKE "Sherlock%";

UPDATE shows
SET
  title = "Squid Game"
WHERE
  title = "squid game";

UPDATE shows
SET
  title = "The Bachelorette"
WHERE
  title = "the bachelorette";

UPDATE shows
SET
  title = "The Crown"
WHERE
  title = "The CROWN";

UPDATE shows
SET
  title = "The Office"
WHERE
  title LIKE "The Office";

UPDATE shows
SET
  title = "The Untamed"
WHERE
  title = "the Untamed";

SELECT
  *
FROM
  shows
ORDER BY
  title;