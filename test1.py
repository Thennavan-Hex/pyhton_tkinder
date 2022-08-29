from tkinter import *
from tkinter import ttk


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1250x700")
        self.login()

    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=30, height=30)
        self.frame1.pack()


        self.register_btn = ttk.Button(self.frame1, text="Start",width=30,padding=10,command=self.level)
        self.register_btn.pack(padx=30,pady=70)
        self.register_btn.pack()

        self.settings_btn = ttk.Button(self.frame1, text="Settings",width=30, padding=10, command=self.level)
        self.settings_btn.pack(padx=30, pady=20)
        self.settings_btn.pack()

        self.exit_btn = ttk.Button(self.frame1, text="Exit", width=30, padding=10, command=self.level)
        self.exit_btn.pack(padx=30, pady=80)
        self.exit_btn.pack()


    def level(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=1250, height=700)
        self.frame2.pack()

        self.easy_btn = ttk.Button(self.frame2, text="Easy",width=30,padding=10, command=self.login)
        self.easy_btn.pack(padx=30,pady=70)
        self.easy_btn.pack()

        self.medium_btn = ttk.Button(self.frame2, text="Medium", width=30, padding=10, command=self.login)
        self.medium_btn.pack(padx=30, pady=20)
        self.medium_btn.pack()

        self.hard_btn = ttk.Button(self.frame2, text="Hard", width=30, padding=10, command=self.login)
        self.hard_btn.pack(padx=30, pady=80)
        self.hard_btn.pack()

        self.insine_btn = ttk.Button(self.frame2, text="Extreme", width=30, padding=10, command=self.login)
        self.insine_btn.pack(padx=30, pady=20)
        self.insine_btn.pack()

        self.back_btn = ttk.Button(self.frame2, text="Back", width=30, padding=10, command=self.login)
        self.back_btn.grid(row=0,column=0)
        self.back_btn.pack()


root = Tk()
app(root)
root.mainloop()