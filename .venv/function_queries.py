avg_in_rng_trap_query = ("SELECT AVG(T.Score) AS Avg_Score, AVG(T.Sta_1) AS Station_1_Avg, AVG(T.Sta_2) AS Station_2_Avg, "
                                "AVG(T.Sta_3) AS Station_3_Avg, AVG(T.Sta_4) AS Station_4_Avg, AVG(T.Sta_5) AS Station_5_Avg "
                        "FROM TRAP_SCORE AS T "
                        "WHERE Ath_ID = %s AND Date BETWEEN %s AND %s")

avg_in_rng_skeet_query = ("SELECT AVG(S.Score) AS Avg_Score, AVG(S.Sta_1) AS Station_1_Avg, AVG(S.Sta_2) AS Station_2_Avg, "
                                "AVG(S.Sta_3) AS Station_3_Avg, AVG(S.Sta_4) AS Station_4_Avg, AVG(S.Sta_5) AS Station_5_Avg, "
                                "AVG(S.Sta_6) AS Station_6_Avg, AVG(S.Sta_7) AS Station_7_Avg, AVG(S.Sta_8) AS Station_8_Avg "
                        "FROM SKEET_SCORE AS S "
                        "WHERE Ath_ID = %s AND Date BETWEEN %s AND %s")

score_bfr_query = ("SELECT AVG(T.Score) AS Avg_Trap_Score_After, AVG(SK.Score) AS Avg_Skeet_Score_After, AVG(SP.Score) AS Avg_Sporting_Clays_Score_After "
                   "FROM TRAP_SCORE AS T, SKEET_SCORE AS SK, SPORTING_CLAYS_SCORE AS SP, WORKS_WITH AS W "
                   "WHERE W.Ath_ID = %s AND W.Cert_no = %s AND T.Date >= W.Start_date AND SK.Date >= W.Start_date AND SP.Date >= W.Start_date ")

score_aftr_query = ("SELECT AVG(T.Score) AS Avg_Trap_Score_Before, AVG(SK.Score) AS Avg_Skeet_Score_Before, AVG(SP.Score) AS Avg_Sporting_Clays_Score_Before "
                    "FROM TRAP_SCORE AS T, SKEET_SCORE AS SK, SPORTING_CLAYS_SCORE AS SP, WORKS_WITH AS W "
                    "WHERE W.Ath_ID = %s AND W.Cert_no = %s AND T.Date < W.Start_date AND SK.Date < W.Start_date AND SP.Date < W.Start_date ")

top_5_trap_ath_query = ("SELECT A.Athlete_ID AS Athlete_ID, A.Name AS Name, AVG(T.Score) AS Avg_Trap_Score "
                        "FROM ATHLETE AS A, TRAP_SCORE AS T "
                        "WHERE A.Athlete_ID = T.Ath_ID AND A.Team_ID = %s "
                        "GROUP BY T.Ath_ID "
                        "ORDER BY AVG(T.Score) DESC "
                        "LIMIT 5")

top_5_skeet_ath_query = ("SELECT A.Athlete_ID AS Athlete_ID, A.Name AS Name, AVG(SK.Score) AS Avg_Skeet_Score "
                         "FROM ATHLETE AS A, SKEET_SCORE AS SK "
                         "WHERE A.Athlete_ID = SK.Ath_ID AND A.Team_ID = %s "
                         "GROUP BY SK.Ath_ID "
                         "ORDER BY AVG(SK.Score) DESC "
                         "LIMIT 5")

top_5_sporting_clays_query = ("SELECT A.Athlete_ID AS Athlete_ID, A.Name AS Name, AVG(SP.Score) AS Avg_Sporting_Clays_Score "
                              "FROM ATHLETE AS A, SPORTING_CLAYS_SCORE AS SP "
                              "WHERE A.Athlete_ID = SP.Ath_ID AND A.Team_ID = %s "
                              "GROUP BY SP.Ath_ID "
                              "ORDER BY AVG(SP.Score) DESC "
                              "LIMIT 5")