import csv
import tkinter as tk
from tkinter import messagebox,ttk
import matplotlib.pyplot as plt
def load_data_and_filter(student_score):
    eligible_colleges=[]
    try:
        with open('cutoff_data.csv', mode='r', encoding='utf-8') as file:
            csv_reader = csv.Dictreader(file)
            for row in csv_reader:
                cutoff_val = float(row['Year_2026'])
                if cutoff_val <= student_score:
                    record = [
                        row['College_Name'],
                        row['Branch'],
                        row['year_2024'],
                        row['year_2025'],
                        row['year_2026']
                    ]
                    eligible_colleges.append(record)
    except FileNotFoundError:
        messagebox.showerror("Error","'cutoff_data.csv' file not found! Please check if file is in the same folder")
    return eligible_colleges

def show_graph(selected_item):
    if not selected_item:
        messagebox.showwarning("Warning","First select a college from the list!")
        return
    #selected row data
    college_name=selected_item[0]
    branch=selected_item[1]
    years=['2024','2025','2026']
    cutoffs=[float(selected_item[2]),float(selected_item[3]),float(selected_item[4])]
    #Matplotlib line graph plot 
    plt.figure(figsize=(6,4))
    plt.plot(years,cutoffs,marker='o',color='b')
