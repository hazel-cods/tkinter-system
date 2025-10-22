import tkinter as tk
from tkinter import ttk, messagebox

# ---------- Login Page --------------
class LoginPage(tk.Frame):
    def __init__(self, master, success_login):
        super().__init__(master)
        self.master = master
        self.success_login = success_login
        self.configure(bg="#758a93")

        tk.Label(self, text="Login Page", bg="#758a93", fg="#ecd5bc", font=("Arial", 16, "bold")).pack(pady=40)
        tk.Label(self, text="    Username", font="arial 13 ", anchor="w", bg="#758a93", fg="#ecd5bc").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="   Password", font="arial 13 ", anchor="w", bg="#758a93", fg="#ecd5bc").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", font="arial 13 ", bg="#758a93", fg="#ecd5bc", width=20, command=self.login).pack(pady=20, padx=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "hazel" and password == "123":
            messagebox.showinfo("Success", "Login successful!")
            self.success_login()
        else:
            messagebox.showerror("Error", "Invalid username or password")


# ---------------- Dashboard ----------------
class Dashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.sidebar = tk.Frame(self,  bg="#758a93", width=400)
        self.sidebar.pack(side="left", fill="y")

        tk.Label(self.sidebar, text="Dashboard", bg="#758a93", font="arial 20 bold",  width=10, fg="#ecd5bc").pack(padx=20, pady=20)

        tk.Button(self.sidebar, text="Profile", bg="#758a93", font="arial 15 ", fg="#ecd5bc", bd=0,
                  command=lambda: self.show_page('profile')).pack(padx=5, fill="x")
        tk.Button(self.sidebar, text="Subjects", bg="#758a93", font="arial 15 ", fg="#ecd5bc", bd=0,
                  command=lambda: self.show_page('subjects')).pack(padx=5, fill="x")
        tk.Button(self.sidebar, text="Schedule", bg="#758a93", font="arial 15 ", fg="#ecd5bc", bd=0,
                  command=lambda: self.show_page('schedule')).pack(padx=5, fill="x")
        tk.Button(self.sidebar, text="Tuition", bg="#758a93", font="arial 15 ", fg="#ecd5bc", bd=0,
                  command=lambda: self.show_page('tuition')).pack(padx=5, fill="x")
        tk.Button(self.sidebar, text="Logout", bg="#758a93", font="arial 15 ", fg="#ecd5bc", bd=0,
                  command=lambda: self.show_page('logout')).pack(padx=5, fill="x")

        self.main_content = tk.Frame(self, bg="#ecd5bc")
        self.main_content.pack(side="right", fill="both", expand=True)

    def show_page(self, page_name):
        pages = {
            "profile": ("#ecd5bc", "Profile Page"),
            "subjects": ("#ecd5bc", "Subject Page"),
            "schedule": ("#ecd5bc", "Schedule Page"),
            "tuition": ("#ecd5bc", "Tuition Page"),
            "logout": ("#ecd5bc", "You've been logged out!"),
        }

        bg_color, text = pages.get(page_name, ("white", "Unknown Page"))

        for widget in self.main_content.winfo_children():
            widget.destroy()

        self.main_content.configure(bg=bg_color)
        tk.Label(self.main_content, text=text, font=("Arial", 20, "bold")).pack(pady=30)


# ---------------- Main App ----------------
class Main_App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard with Login Auth")
        self.geometry("800x500")

        self.login_page = LoginPage(self, self.show_dashboard)
        self.dashboard_page = Dashboard(self)

        self.login_page.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.login_page.pack_forget()
        self.dashboard_page.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = Main_App()
    app.mainloop()
