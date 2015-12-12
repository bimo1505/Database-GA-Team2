# Database-GA-Team2
Group Assignment Repo for Database Class

Team 2 Responsibilities :

> **Aji** Documentation // **Bimo** Database Setup // **Meta** Main Program // **Revin** GUI

----------

#### Main Program Notes
- For deleting and updating a table row, the row is chosen in the SQL query based on its primary key, as it is the least likely attribute to be changed. So when the user would like to update a table row, they should be prohibited from updating the primary key.
- The primary key should be the first column on every table in order to make fetching it easier.

#### GUI Notes
- Make a validation for when no tables have been chosen but the user still tries to click on a command button.
- For **Create Entry**, the program provides text boxes for every column.
- For **Update Entry**, the program provides text boxes for every column except the primary key and a dropdown menu of all entries from the primary key column.
- For **Delete Entry**, the program lists all entries from the primary key column. The primary key entry that gets chosen will have its corresponding row deleted.
