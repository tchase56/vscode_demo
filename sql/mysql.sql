-- Create a Table in SQLite DB mydb.db
CREATE TABLE example_table(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Insert some data into the table
INSERT INTO example_table(id, name) 
VALUES(1, 'John'),
      (2, 'Jane'),
      (3, 'Bob'),
      (4, 'Alice');

-- Query the table
SELECT * FROM example_table;

-- Delete the table
DROP TABLE example_table;