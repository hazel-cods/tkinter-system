import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)





window = ttk.Window(themename= 'darkly')
window.title("Sample")
window.geometry("300x150")
window.resizable(False, False)

#title
title_label = ttk.Label(master = window, text="Title here!", font ="Arial 20 bold")
title_label.pack(pady=5)

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text="convert", command= convert)
entry.pack(side="left", padx = 5)
button.pack(side="left")
input_frame.pack(pady = 5)


#output label
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text="Output", font="Arial 20 ", textvariable= output_string)
output_label.pack()







window.mainloop()










#---------------------------------------------------------DAY 2 -----------PRACTICE -----------------------------------------------------------


import tkinter as tk 
from tkinter import ttk


window = tk.Tk()
window.title("Web App System")
window.geometry("1000x650")
window.config(bg="#faeab1")
window.resizable(True, True)




#--------------LOGIN PAGE------------------------------------------









#---------------DASHBOARD PAGE-------------------------------------------
class dashboardApp():
    def __init__(self, master):
        self.master = master


        #-------sidebar-----------------------------
        self.side_frame = tk.Frame(master = self.master, bg="#432323", width=200)
        self.side_frame.pack(side="left" ,fill="y")


        self.main_frame = tk.Frame(master= self.master, bg="#334443" )
        self.main_frame.pack(side="right", fill="both", expand=True)

        #--------Configure------------------------------
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        
        





        #-----------sidebar & buttons design----------------------------------------
        title_label = tk.Label(master = self.side_frame, text="Dashboard", font="Arial 20 bold " , bg="#432323", fg="#34656d", bd=0)
        title_label.pack(padx=30, pady=40)

        btn_home = tk.Button(master= self.side_frame, text="Home", font="Arial 14  ", bg="#432323", fg="#34656d", bd=0, width=15, command= self.show_home )
        btn_home.pack( pady=5)

        btn_profile = tk.Button(master= self.side_frame, text="Profile", font="Arial 14  ", bg="#432323", fg="#34656d", bd=0, width=15, command= self.show_profile )
        btn_profile.pack(padx=3, pady=5)

        btn_subject = tk.Button(master= self.side_frame, text="Subject", font="Arial 14  ",  bg="#432323", fg="#34656d", bd=0, width=15, command= self.show_subject  )
        btn_subject.pack(padx=2, pady=5)

        btn_schedule = tk.Button(master= self.side_frame, text="Schedule", font="Arial 14  ",  bg="#432323", fg="#34656d", bd=0, width=15, command= self.show_schedule  )
        btn_schedule.pack(padx=2, pady=3)

        btn_settings = tk.Button(master= self.side_frame, text="Settings", font="Arial 14  ",  bg="#432323", fg="#34656d", bd=0, width=15, command= self.show_settings )
        btn_settings.pack(padx=2, pady=5)

        btn_logout = tk.Button(master= self.side_frame, text="Logout", font="Arial 14  ",  bg="#432323", fg="#34656d", bd=0, width=15, command= self.show_logout  )
        btn_logout.pack(padx=2, pady=5)

        self.show_home()





    #--------------FUNCTIONS----------------------------


    #-------------helper function to clear main page-----------------------------
    def clear_main_frame(self):
        #clear all widgets in main content
        for widget in self.main_frame.winfo_children():
            widget.destroy()





    

    #----------Function & Design for sidebar buttons--------------------------------------------------------------
    def show_home(self):
        self.clear_main_frame()
        self.main_frame.config(bg="#334443")
        tk.Label(master= self.main_frame, text="Home Page", font="Arial 15 bold", bg="#334443" , fg="#faeab1").pack(pady=100)


    def show_profile(self):
        self.clear_main_frame()
        self.main_frame.config(bg="#334443")
        tk.Label(master= self.main_frame, text="Profile Page", font="Arial 15 bold", bg="#334443" , fg="#faeab1").pack(pady=100)

    def show_subject(self):
        self.clear_main_frame()
        self.main_frame.config(bg="#334443")
        tk.Label(master= self.main_frame, text="Subject Page", font="Arial 15 bold", bg="#334443" , fg="#faeab1").pack(pady=100)

    def show_schedule(self):
        self.clear_main_frame()
        self.main_frame.config(bg="#334443")
        tk.Label(master= self.main_frame, text="Schedule Page", font="Arial 15 bold", bg="#334443" , fg="#faeab1").pack(pady=100)

    def show_settings(self):
        self.clear_main_frame()
        self.main_frame.config(bg="#334443")
        tk.Label(master= self.main_frame, text="Settings Page", font="Arial 15 bold", bg="#334443" , fg="#faeab1").pack(pady=100)

    def show_logout(self):
        self.clear_main_frame()
        self.main_frame.config(bg="#334443")
        tk.Label(master= self.main_frame, text="Logout Page", font="Arial 15 bold", bg="#334443" , fg="#faeab1").pack(pady=100)






#close the class
app = dashboardApp(window)
window.mainloop()









