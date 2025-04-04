# SQLite Database Interaction Scripts

This repository contains five Python scripts for interacting with an SQLite database named `sampleDB.db` and a table named `sampleTable`. The table `sampleTable` contains five columns: `id`, `name`, `address`, `year`, and `color`. The `id` and `year` columns store integer values.

## Files

1.  **`read_tables.py`:**
    * This script reads and prints the names of all tables present in the `sampleDB.db` database.
    * It uses the `sqlite_master` table to retrieve table names.
    * It outputs the table names to the terminal.

2.  **`read_data.py`:**
    * This script reads and prints all records from the `sampleTable` table.
    * It retrieves all columns and rows from the table.
    * It outputs the data to the terminal.

3.  **`create_record_gui.py`:**
    * This script provides a graphical user interface (GUI) for creating new records in the `sampleTable` table.
    * It uses Tkinter for the GUI.
    * It allows the user to enter values for the `id`, `name`, `address`, `year`, and `color` columns.
    * It includes error handling for data type mismatches.
    * Once the submit button is pressed, the text boxes are cleared, and a message is printed to the terminal.
    * ID and year are treated as integer inputs.

4.  **`update_record_gui.py`:**
    * This script provides a GUI for updating existing records in the `sampleTable` table.
    * It updates the name, address, year, and color columns, based on the ID.
    * It uses Tkinter for the GUI.
    * It requires the user to enter the `id` of the record to be updated, as well as the new values for the `name`, `address`, `year`, and `color` columns.
    * It includes error handling for data type mismatches.
    * Once the update button is pressed, the text boxes are cleared, and a message is printed to the terminal.
    * ID and year are treated as integer inputs.

5.  **`delete_record_gui.py`:**
    * This script provides a GUI for deleting records from the `sampleTable` table.
    * It uses Tkinter for the GUI.
    * It requires the user to enter the `id` of the record to be deleted.
    * It includes error handling for invalid input.
    * Once the delete button is pressed, the text boxes are cleared, and a message is printed to the terminal.
    * ID is treated as an integer input.

## Prerequisites

* Python 3.x
* SQLite 3
* Tkinter (usually included with Python)

## Usage

1.  **Ensure the database and table exist:**
    * Create `sampleDB.db` and `sampleTable` with the appropriate columns if they don't already exist. You can use an SQLite browser or write a python script to do this.
2.  **Run the scripts:**
    * Execute the Python scripts from your terminal using `python <filename>.py`.
    * For the GUI files, the GUI window will appear.
3.  **Interact with the GUI (for create, update, delete):**
    * Enter the required information in the entry fields.
    * Click the "Submit," "Update," or "Delete" button.
    * Follow the on-screen instructions and messages.
4.  **Observe terminal output (for read files, and confirmation of GUI actions):**
    * The terminal will print the results of the database operations.
    * The terminal will also display error messages if any occur.

## Important Notes

* Ensure that the data types entered in the GUI match the data types of the corresponding columns in the `sampleTable` table.
* The `id` column is used to identify records for updating and deleting.
* The scripts use parameterized queries to help prevent SQL injection vulnerabilities.
* The scripts include error handling to ensure data integrity.
* The database file, and table name are hard coded into the python files. If you wish to use different names, you will have to change the python files.