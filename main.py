import tkinter as tk
from tkinter import messagebox

# ---------------- LOGIN PAGE ---------------- #
class LoginPage(tk.Frame):
    def __init__(self, master, on_login_success):
        super().__init__(master)
        self.master = master
        self.on_login_success = on_login_success
        self.configure(bg="#34656d")

        tk.Label(self, text="Welcome", font=("Arial", 22, "bold"), bg="#34656d").pack(pady=20)
        tk.Label(self, text="Username", bg="#34656d").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password", bg="#34656d").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", bg="#4c70d4", fg="white", command=self.check_login).pack(pady=15)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "1234":
            messagebox.showinfo("Success", "Login Successful!")
            self.on_login_success()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

# ---------------- DASHBOARD PAGE ---------------- #
class DashboardApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Sidebar
        sidebar = tk.Frame(self, bg="#432323", width=400)
        sidebar.pack(side="left", fill="y")

        tk.Label(master = sidebar, text="Dashboard", font="Arial 20 bold " , bg="#432323", fg="#faeab1", bd=0).pack(padx=30, pady=40)

        tk.Button(sidebar, text="Profile", bg="#432323", fg="#faeab1", bd=0, command=lambda: self.show_page("profile")).pack(fill="x", pady=5)
        tk.Button(sidebar, text="Subjects", bg="#432323", fg="#faeab1", bd=0, command=lambda: self.show_page("subjects")).pack(fill="x", pady=5)

        # Main content area
        self.main_frame = tk.Frame(self, bg="#334443")
        self.main_frame.pack(side="right", fill="both", expand=True)

    def show_page(self, page):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if page == "profile":
            self.main_frame.config(bg="#faeab1")
            tk.Label(self.main_frame, text="Profile Page", bg="#faeab1", font=("Arial", 18, "bold")).pack(pady=50)
        elif page == "subjects":
            self.main_frame.config(bg="#faeab1")
            tk.Label(self.main_frame, text="Subjects Page", bg="#faeab1", font=("Arial", 18, "bold")).pack(pady=50)

# ---------------- MAIN APP ---------------- #
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("School Dashboard System")
        self.geometry("800x500")

        self.login_page = LoginPage(self, self.show_dashboard)
        self.dashboard = DashboardApp(self)

        self.login_page.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.login_page.pack_forget()
        self.dashboard.pack(fill="both", expand=True)

# ---------------- RUN APP ---------------- #
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
