import customtkinter as ctk
from customtkinter import CTkImage
from PIL import ImageTk, Image
import cv2
import backend
import modules.connection
app=ctk.CTk()
app.title("pharmacy inventory")
app.geometry("1910x1000")


def everything():
    def adddataframe():
        h=app.winfo_width()
        w=app.winfo_height()
        dataframe=ctk.CTkFrame(app,corner_radius=20,height=h*0.8,width=w*0.8,fg_color="gray")
        dataframe.place(relx=0.5, rely=0.5, anchor="center")
    def adddata(data):
        backend.insert_data(data)
    
    def add_col(col,name):
        header=ctk.CTkLabel(table, text=name,font=("Arial", 14, "bold"),fg_color="#205E77",corner_radius=5,height=40)
        header.grid(row=0, column=col,padx=3,pady=3,sticky="ew")

    def add_row(col,row,data):
        cell=ctk.CTkLabel(scroll,text=data,height=35)
        cell.grid(row=row,column=col,sticky="ew",padx=5,pady=5)


    main=ctk.CTkFrame(app,corner_radius=15)
    main.pack(fill="both", expand=True, padx=20, pady=20)

    title_frame=ctk.CTkFrame(main, corner_radius=15,fg_color="transparent")
    title_frame.pack(fill="x", padx=20, pady=5)

    title=ctk.CTkLabel(title_frame,text="Pharmacy Management System",font=("Arial", 40, "bold"),anchor="w",fg_color="transparent")
    title.pack(fill="x",padx=30,pady=(30,5))

    content = ctk.CTkFrame(main, fg_color="transparent")
    content.pack(fill="both", expand=True, padx=20, pady=5)


    menu = ctk.CTkFrame(content, corner_radius=15, width=180)
    menu.pack(side="right", fill="y", padx=5, pady=5)
    menu.pack_propagate(False)

    edimg=CTkImage(light_image=Image.open("gng/local pharmacy inventory/assets/pencil-edit-svgrepo-com(1).png"),
                                  dark_image=Image.open("gng/local pharmacy inventory/assets/pencil-edit-svgrepo-com(1)_dark.png"))
    adimg=CTkImage(light_image=Image.open("gng/local pharmacy inventory/assets/plus-svgrepo-com.png"),
                                      dark_image=Image.open("gng/local pharmacy inventory/assets/plus-svgrepo-com_dark.png"))
    edit = ctk.CTkButton(menu, text=None,image=edimg,height=80,width=80)
    edit.pack(pady=5)

    add = ctk.CTkButton(menu,height=40,width=40, text=None,image=adimg,fg_color="transparent",command=adddataframe)
    add.pack(pady=5)

    sort = ctk.CTkButton(menu,height=40,width=40, text="Sort",fg_color="transparent")
    sort.pack(pady=5)

    remove = ctk.CTkButton(menu,height=40,width=40, text="Remove",fg_color="transparent")
    remove.pack(pady=5)

    export = ctk.CTkButton(menu,height=40,width=40, text="Export",fg_color="transparent")
    export.pack(pady=5)


    table=ctk.CTkFrame(content, corner_radius=10)
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
login_frame = ctk.CTkFrame(app, fg_color="transparent")
login_frame.pack(fill="both", expand=True)

login_box = ctk.CTkFrame(login_frame, corner_radius=15)
login_box.place(relx=0.5, rely=0.5, anchor="center")

title = ctk.CTkLabel(
    login_box,
    text="Pharmacy Login",
    font=("Arial", 30, "bold")
)
title.pack(padx=30, pady=(25, 20))

def login():
    password_entry.unbind("<Return>")
    password = password_entry.get()
    backend.passwd(password)

    login_frame.pack_forget()
    everything()
    

password_entry = ctk.CTkEntry(
    login_box,
    placeholder_text="MySQL password",
    show="*",
    width=300
)
password_entry.pack(padx=30, pady=10)
password_entry.focus_set()
password_entry.bind("<Return>", lambda event: login())
ok = ctk.CTkButton(
    login_box,
    text="OK",
    command=login
)
ok.pack(pady=15)


app.mainloop()
modules.connection.close(backend.cur,backend.con)