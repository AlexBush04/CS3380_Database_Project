### Initialize the Database
This step only needs to be done once. Using the MySQL Workbench, or however you interact with MySQL on your machine, run the clay_target_data_Table&Insert_Statements.sql file in your local instance of
MySQL. This will create the clay_target_data database schema, all of the schema's tables, and will populate the tables with initial data.

### Run Application
Open the GUI_interface.py file (in the .venv folder) in a Python instance and run it. A user interface should open up and allow you to interact with the database. If you open up the Application_functions.py file and look in
main() function, you will find commented out function calls. You can use the parameters from these function calls to test the application, or you can go into the clay_target_data_Table&Insert_Statements
file and search through the insert statments to find other parameters you can use with the functions.
