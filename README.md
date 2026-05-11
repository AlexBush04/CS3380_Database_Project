### Initialize the Database
This step only needs to be done once. Using the MySQL Workbench, or however you interact with MySQL on your machine, run the clay_target_data_Table&Insert_Statements.sql file in your local instance of
MySQL. This will create the clay_target_data database schema, all of the schema's tables, and will populate the tables with initial data.

### Run Application
Open the GUI_interface.py file (in the .venv folder) in a Python instance. Before running the application, you need to alter the connection_info in the __init__() function. Where it says "YOUR USERNAME FOR YOUR SQL INSTANCE", enter whatever username is required to connect to your local instance of MySQL. Where it says "YOUR PASSWORD HERE", enter your MySQL password that you would normally enter when accessing your MySQL instance. Where it says "THE NAME OF YOUR LOCAL SQL INSTANCE OR YOUR IP-ADDRESS", you need to enter the name of your local MySQL instance or your IP address.
DO NOT CHANGE THE DATABASE BEING CONNECTED TO!
Once these changes have been made, you can run this application file.

If you have made these changes successfully, then a user interface should open up and allow you to interact with the database. If you open up the Application_functions.py file and look in main() function, you will find commented out function calls. You can use the parameters from these function calls to test the application, or you can go into the clay_target_data_Table&Insert_Statements file and search through the insert statments to find other parameters you can use with the functions.
