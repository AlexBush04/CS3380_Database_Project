"""
Note: All of the code in this file was AI generated using Gemini
"""

import tkinter as tk
from tkinter import ttk, messagebox
from Database_connection import open_connection, close_connection
import Application_functions as af

class ShotgunDatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Shotgun Sports Athlete Management")
        self.root.geometry("900x600")

        # 1. Database Connection Setup
        # Using the credentials provided in your Application_functions.py main()
        self.connection_info = {
            "user": "YOUR USERNAME FOR YOUR SQL INSTANCE",
            "password": "YOUR PASSWORD HERE",
            "host": "THE NAME OF YOUR LOCAL SQL INSTANCE OR YOUR IP-ADDRESS",
            "database": "clay_target_data"
        }
        
        self.cnx = open_connection(self.connection_info)
        if self.cnx and self.cnx.is_connected():
            self.executor = self.cnx.cursor()
        else:
            messagebox.showerror("Connection Error", "Could not connect to the local database.")
            self.root.destroy()
            return

        # 2. UI Layout - Notebook for Tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Create Tab Frames
        self.tab_avg = ttk.Frame(self.notebook)
        self.tab_coach = ttk.Frame(self.notebook)
        self.tab_top5 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_avg, text="Range Averages")
        self.notebook.add(self.tab_coach, text="Coaching Progress")
        self.notebook.add(self.tab_top5, text="Top Athletes")

        # Initialize UI for each tab
        self.init_avg_tab()
        self.init_coach_tab()
        self.init_top5_tab()

        # Handle proper closure of DB connection when window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def init_avg_tab(self):
        """UI for average_in_range()"""
        input_frame = ttk.LabelFrame(self.tab_avg, text="Query Parameters")
        input_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(input_frame, text="Athlete ID:").grid(row=0, column=0, padx=5, pady=5)
        self.avg_ath_id = ttk.Entry(input_frame)
        self.avg_ath_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Game Type:").grid(row=0, column=2, padx=5, pady=5)
        self.game_var = ttk.Combobox(input_frame, values=["Trap", "Skeet"])
        self.game_var.set("Trap")
        self.game_var.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Start (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.start_date = ttk.Entry(input_frame)
        self.start_date.insert(0, "2022-01-01")
        self.start_date.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="End (YYYY-MM-DD):").grid(row=1, column=2, padx=5, pady=5)
        self.end_date = ttk.Entry(input_frame)
        self.end_date.insert(0, "2025-12-31")
        self.end_date.grid(row=1, column=3, padx=5, pady=5)

        ttk.Button(input_frame, text="Fetch Averages", command=self.run_avg_range).grid(row=2, column=0, columnspan=4, pady=10)

        self.avg_tree = ttk.Treeview(self.tab_avg, columns=("Stat", "Value"), show="headings")
        self.avg_tree.heading("Stat", text="Station/Total")
        self.avg_tree.heading("Value", text="Average Score")
        self.avg_tree.pack(expand=True, fill="both", padx=10, pady=10)

    def init_coach_tab(self):
        """UI for score_before_and_after()"""
        input_frame = ttk.LabelFrame(self.tab_coach, text="Coaching Analysis")
        input_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(input_frame, text="Athlete ID:").grid(row=0, column=0, padx=5, pady=5)
        self.coach_ath_id = ttk.Entry(input_frame)
        self.coach_ath_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Coach Cert #:").grid(row=0, column=2, padx=5, pady=5)
        self.cert_no = ttk.Entry(input_frame)
        self.cert_no.grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(input_frame, text="Compare Scores", command=self.run_coach_compare).grid(row=1, column=0, columnspan=4, pady=10)

        self.coach_tree = ttk.Treeview(self.tab_coach, columns=("Period", "Trap Avg", "Skeet Avg", "Clays Avg"), show="headings")
        for col in self.coach_tree["columns"]:
            self.coach_tree.heading(col, text=col)
        self.coach_tree.pack(expand=True, fill="both", padx=10, pady=10)

    def init_top5_tab(self):
        """UI for top_5_athletes() with separate tables for each game."""
        # Top-level control frame
        controls = ttk.Frame(self.tab_top5)
        controls.pack(fill="x", padx=10, pady=5)

        ttk.Label(controls, text="Team ID:").pack(side="left", padx=5)
        self.team_id = ttk.Entry(controls)
        self.team_id.pack(side="left", padx=5)

        ttk.Button(controls, text="Get All Leaders", command=self.run_top_5).pack(side="left", padx=5)

        # Create a Sub-Notebook inside the Top Athletes tab
        self.sub_notebook = ttk.Notebook(self.tab_top5)
        self.sub_notebook.pack(expand=True, fill="both", padx=5, pady=5)

        # Create frames for each sub-tab
        self.tab_trap = ttk.Frame(self.sub_notebook)
        self.tab_skeet = ttk.Frame(self.sub_notebook)
        self.tab_clays = ttk.Frame(self.sub_notebook)

        self.sub_notebook.add(self.tab_trap, text="Trap")
        self.sub_notebook.add(self.tab_skeet, text="Skeet")
        self.sub_notebook.add(self.tab_clays, text="Sporting Clays")

        # Dictionary to hold the three separate Treeviews
        self.top_trees = {}
        cols = ("Athlete ID", "Name", "Avg Score")

        for game, frame in [("Trap", self.tab_trap), ("Skeet", self.tab_skeet), ("Sporting Clays", self.tab_clays)]:
            tree = ttk.Treeview(frame, columns=cols, show="headings")
            for col in cols:
                tree.heading(col, text=col)
                tree.column(col, anchor="center")
            tree.pack(expand=True, fill="both", padx=5, pady=5)
            self.top_trees[game] = tree

    # --- Backend Execution Logic ---

    def run_avg_range(self):
        # Calls af.average_in_range
        data = af.average_in_range(self.executor, self.start_date.get(), self.end_date.get(), 
                                   self.game_var.get(), self.avg_ath_id.get())
        
        for i in self.avg_tree.get_children(): self.avg_tree.delete(i)
        if data:
            labels = ["Overall Avg", "Station 1", "Station 2", "Station 3", "Station 4", "Station 5"]
            if self.game_var.get() == "Skeet":
                labels += ["Station 6", "Station 7", "Station 8"]
            
            for label, val in zip(labels, data):
                self.avg_tree.insert("", "end", values=(label, f"{val:.2f}" if val else "N/A"))
        else:
            messagebox.showinfo("No Data", "No records found for this athlete in the specified range.")

    def run_coach_compare(self):
        # Calls af.score_before_and_after
        results = af.score_before_and_after(self.executor, self.coach_ath_id.get(), self.cert_no.get())
        
        for i in self.coach_tree.get_children(): self.coach_tree.delete(i)
        for period in ["before", "after"]:
            if results[period]:
                self.coach_tree.insert("", "end", values=(period.capitalize(), *results[period]))

    def run_top_5(self):
        # Calls af.top_5_athletes which returns {"Trap": [...], "Skeet": [...], "Sporting Clays": [...]}
        data = af.top_5_athletes(self.executor, self.team_id.get())
        
        # Iterate through each game type and its specific Treeview
        for game_type, athletes in data.items():
            tree = self.top_trees[game_type]
            
            # Clear this specific table
            for i in tree.get_children():
                tree.delete(i)
                
            # Populate this specific table
            for athlete in athletes:
                # athlete tuple contains: (Athlete_ID, Name, Avg_Score)
                tree.insert("", "end", values=athlete)

    def on_close(self):
        close_connection(self.cnx, self.executor)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShotgunDatabaseGUI(root)
    root.mainloop()