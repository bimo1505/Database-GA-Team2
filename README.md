# Database-GA-Team2
Group Assignment Repo for Database Class

Team 2 Responsibilities :

> **Aji** Documentation // **Bimo** Database Setup // **Meta** Main Program // **Revin** GUI

----------

#### Main Program Notes
- For deleting and updating a table row, the row is chosen in the SQL query based on its primary key, as it is the least likely attribute to be changed. So when the user would like to update a table row, they should be prohibited from updating the primary key.
- The primary key should be the first column on every table in order to make fetching it easier.

#### GUI Notes
- For **Create Entry**, the program provides text boxes for every column.
- For **Update Entry**, the program provides text boxes for every column except the primary key. 
- For **Delete Entry**, the program lists all entries from the primary key column. The primary key entry that gets chosen will have its corresponding row deleted.
