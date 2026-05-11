"""
Name: Alex Bush
Program: Connection application between a localized database that contains information about shotgun sport teams and their
         athletes.

General Note: Information about how to use the MySQL connector and its functions came from the official mysql documentation.
              Link to this documentation can be found here: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
            
Note on AI Usage: The GUI for this application was developed using Gemini AI. Using said AI, I altered how the average_in_range(), score_before_and_after(),
                  and top_5_athletes() functions return data to work with a GUI library. The file GUI_interface was also added per the AI advice to handle
                  all of the GUI functions separately from the application logic.
                  
                  The link to my chat page is here: https://gemini.google.com/app/760b0e0661463c61
"""

# from Database_connection import open_connection       No longer needed in this file because the connection is handled in GUI_interface.py
# from Database_connection import close_connection      No longer needed in this file because the connection is handled in GUI_interface.py
import function_queries

"""
This function retrieves an athlete's average round score and individual station averages for a given time period.
This function only retrieves the average scores for trap or skeet
"""
def average_in_range(executor, start_date, end_date, game, ath_id):
    # If the game that is passed to this function is "trap" then execute the avg_in_rng_trap_query from the function_queries file
    if(game.lower() == "trap"):
        executor.execute(function_queries.avg_in_rng_trap_query, (ath_id, start_date, end_date))
        # AI addition to work with GUI_interface.py
        return executor.fetchone()

    # If the game that is passed to this function is not "trap" then execute the avg_in_rng_skeet_query from the function_queries file
    else:
        executor.execute(function_queries.avg_in_rng_skeet_query, (ath_id, start_date, end_date))
        # AI addition to work with GUI_interface.py
        return executor.fetchone()

"""
This function returns an athlete's average trap, skeet, and sporting clays scores from both before and after they
started working with a specific coach.
"""
def score_before_and_after(executor, ath_id, cert_no):
    # Retrieve the scores after the athlete and coach started working together
    executor.execute(function_queries.score_aftr_query, (ath_id, cert_no))
    after_data = executor.fetchone() # AI addition to work with GUI_interface.py

    # Retrieve the scores before the athlete and coach started working together
    executor.execute(function_queries.score_bfr_query, (ath_id, cert_no))
    before_data = executor.fetchone() # AI addition to work with GUI_inteface.py

    # AI generated way to return data
    return {"after": after_data, "before": before_data}

"""
This function finds a team's top 5 athletes in trap, skeet, and sporting clays based on the athlete's average score in each game.
"""
def top_5_athletes(executor, team_id):
    # Get data on top 5 trap athletes
    executor.execute(function_queries.top_5_trap_ath_query, (team_id,))
    trap_data = executor.fetchall() # AI addition to work with GUI_inteface.py
    
    # Get data on top 5 skeet athletes
    executor.execute(function_queries.top_5_skeet_ath_query, (team_id,))
    skeet_data = executor.fetchall()    # AI addition to work with GUI_inteface.py

    # Get data on top 5 sporting clays athletes
    executor.execute(function_queries.top_5_sporting_clays_query, (team_id,))
    sporting_clays_data = executor.fetchall()   # AI addition to work with GUI_inteface.py

    # AI generated way to return data
    return {"Trap": trap_data, "Skeet": skeet_data, "Sporting Clays": sporting_clays_data}

"""
This main function was written by me to get the logic of the functions working. Per AI suggestion, I have
moved the controll of the application to the GUI_interface file, so this main function is no longer necessary.
"""
# def main():
#     # Dictionary of values required to establish a connection to local MySQL server
#     connection_info = {"user":"YOUR USERNAME FOR YOUR SQL INSTANCE","password":"YOUR PASSWORD HERE",
#                        "host":"THE NAME OF YOUR LOCAL SQL INSTANCE OR YOUR IP-ADDRESS","database":"clay_target_data"}

#     active_cnx = open_connection(connection_info)

#     if(active_cnx and active_cnx.is_connected()):
#         executor = active_cnx.cursor()

#         average_in_range(executor, "2022-01-01", "2025-12-18", "trap", "2222-33333")
#         print()
        
#         average_in_range(executor, "2022-01-01", "2025-12-18", "skeet", "4444-55555")
#         print()

#         score_before_and_after(executor, "4444-55555", "2222-88888")
#         print()

#         top_5_athletes(executor, "1234-5678")
        
#         close_connection(active_cnx, executor)
#     else:
#         print("Failed to connect.")

# main()