import customtkinter as ctk
import backend
import modules.connection
app=ctk.CTk()

def add_col(col,name):
    header=ctk.CTkLabel(table, text=name,font=("Arial", 14, "bold"),fg_color="#205E77",corner_radius=5,height=40)
    header.grid(row=0, column=col,padx=3,pady=3,sticky="ew")

def add_row(col,row,data):
    cell=ctk.CTkLabel(scroll,text=data,height=35)
    cell.grid(row=row,column=col,sticky="ew",padx=5,pady=5)

app.title("pharmacy inventory")
app.geometry("1910x1000")

main=ctk.CTkFrame(app,corner_radius=15)
main.pack(fill="both", expand=True, padx=20, pady=20)

table=ctk.CTkFrame(main, corner_radius=10)
table.pack(fill="both", expand=True, padx=20, pady=20)
table.grid_rowconfigure(1, weight=1)

col=0
colname=backend.colname()
for name in colname:
    add_col(col,name)
    col+=1

for col in range(len(colname)):
    table.grid_columnconfigure(col,weight=1,uniform="columns")

scroll=ctk.CTkScrollableFrame(table,corner_radius= 10)
scroll.grid(row=1,column=0,columnspan=len(colname),sticky="nsew", padx=3, pady=3)

for col in range(len(colname)):
    scroll.grid_columnconfigure(col, weight=1, uniform="columns")

roww = 0

for j in backend.all_data():
    for col in range(len(colname)):
        add_row(col, roww, j[col])

    roww += 1

app.mainloop()
modules.connection.close(backend.cur,backend.con)