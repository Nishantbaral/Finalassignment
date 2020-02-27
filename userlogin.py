from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle

class Employee_management_system:
    def __init__(self):
        '''This class configures and populates the main tkinter window.
           :param
           root - This parameter supports the Tk() {Toplevel window}'''

        self.root = Tk()
        self.root.attributes("-a",0.95)
        self.root.geometry("821x514+264+46")
        self.root.resizable(0, 0)
        self.root.title("Employee Management System")
        self.root.configure(background="#6932a8")

        self.mainframe = Frame(self.root,relief="groove",bd = "2",bg = "#ffffff")
        self.mainframe.place(relx=0.004, rely=0.008, relheight=0.982
                , relwidth=0.993)

        self.title_label = Label(self.mainframe,bg ="#6932a8",font = "Algerian 20",
                            text = "Employee Management system")
        self.title_label.place(relx=0.012, rely=0.02, height=57, width=795)
        self.pointed = []
        try:
            f = open("registration=.txt","rb+")
            pickle.load(f)
            self.indicator = 1
            self.login_interface()
        except Exception:
            self.indicator = 0
            self.registration()

    def login_interface(self):
        """Login interface designing interface are here.
        :return None
        """

        self.sec_frame = Frame(self.mainframe,relief="groove",bd="2",bg="#6932a8")
        self.sec_frame.place(relx=0.015, rely=0.143, relheight=0.842, relwidth=0.975)

        self.loginpage_frame = Frame(self.sec_frame,relief = "groove",bd = "2",bg ="#6932a8")
        self.loginpage_frame.place(relx=0.257, rely=0.009, relheight=0.976, relwidth=0.497)

        icon = PhotoImage(file = "icon.png")
        self.usericon_lbl = Label(self.loginpage_frame,image = icon,bg ="#6932a8")
        self.usericon_lbl.place(relx=0.314, rely=0.036, height=166, width=176)
        self.login_btn = ttk.Button(self.loginpage_frame,takefocus = "",text = "Login",
                                    command = self.Validation)
        self.login_btn.place(relx=0.423, rely=0.805, height=34, width=124)

        self.username_ent = ttk.Entry(self.loginpage_frame,cursor = "xterm",takefocus= "")
        self.username_ent.place(relx=0.362, rely=0.518, relheight=0.065
                , relwidth=0.542)
        self.username_ent.focus()

        self.password_ent = ttk.Entry(self.loginpage_frame,cursor="xterm",takefocus = "",show = "*")
        self.password_ent.place(relx=0.365, rely=0.619, relheight=0.065
                , relwidth=0.542)

        self.Label4 = Label(self.loginpage_frame,text = "Username :",font = "Arial 10",
                            bg = "#6932a8",fg = "#ffffff")

        self.Label4.place(relx=0.081, rely=0.52, height=27, width=95)

        self.password_lbl = Label(self.loginpage_frame,bg = "#6932a8",fg = "#ffffff",
                              text = "Password:",font = "Arial 10")
        self.password_lbl.place(relx=0.084, rely=0.614, height=27, width=95)

        self.help_lbl = Label(self.loginpage_frame,text = "Problem logging in ?", bg = "#6932a8",
                            fg = "#ffffff",cursor = "hand2")
        self.help_lbl.place(relx=0.666, rely=0.718, height=17, width=125)
        self.help_lbl.bind("<Button-1>",self.help_window)#binding label
        self.root.mainloop()
    def help_window(self,*args):
        """"Shows information for one who are in trouble to log in
        :return None
        """

        messagebox.showinfo("Contact !","Please contact system administrator for help.")

    def Validation(self):
        """
        Validates the info given by users.
        :return None
        """
        self.user_get = str(self.username_ent.get())
        b = str(self.password_ent.get())
        data_load = open("reg.txt","rb+")
        test = pickle.load(data_load)
        authenticate = {}
        for i in test:
            username = i["username"]
            password = i["password"]
            authenticate.update({username:password})
        usrs = []
        for i in authenticate:
            usrs.append(i.upper())
        if self.user_get.upper() in usrs:
            if authenticate[self.user_get.upper()] == b:
                self.login_interface_1st()
            else:
                messagebox.showinfo("Error !", "Wrong password")
                self.password_ent.delete(0,END)
                self.password_ent.focus()
        else:
            messagebox.showerror("Error !","Wrong Username")
            self.username_ent.delete(0,END)
            self.password_ent.delete(0,END)
            self.username_ent.focus()

    def registration(self):
        """
        Method for registering users
        :return None
        """
        font10 = "-family P052 -size 12 -weight bold"
        font13 = "-family {Source Code Pro} -size 12 "
        font9 = "-family {Source Code Pro} -size 14 -weight bold "

        self.registration_frame = Frame(self.mainframe, relief="groove", bg="#6932a8", bd=2)
        self.registration_frame.place(relx=0.010, rely=0.150, relheight=0.830, relwidth=0.981)
        if self.indicator == 1:
            self.btn = Button(self.registration_frame,text = "back",bg="#6932a8",command = self.back_reg)
            self.btn.place(relx=0.02, rely=0.911, height=30, width=50)
        else:
            pass


        self.usr_reg_title = Label(self.registration_frame,bg="#6932a8",fg="#ffffff",font=font9,
                                   text = "User Registration")

        self.usr_reg_title.place(relx=0.222, rely=0.03, height=47, width=355)

        self.Separator_horizontal = ttk.Separator(self.registration_frame)
        self.Separator_horizontal.place(relx=0.011, rely=0.863, relwidth=0.969)

        self.name_lbl = Label(self.registration_frame,font=font10,bg="#6932a8",text="Name :")
        self.name_lbl.place(relx=0.234, rely=0.218, height=27, width=75)

        self.name_ent = Entry(self.registration_frame)
        self.name_ent.place(relx=0.333, rely=0.215, height=29, relwidth=0.293)

        self.mobile_lbl_reg = Label(self.registration_frame,bg="#6932a8",text="Employee ID :",font=font10)
        self.mobile_lbl_reg.place(relx=0.200, rely=0.337, height=27, width=105)

        self.test = StringVar()
        self.mobile_ent = Entry(self.registration_frame,textvariable = self.test)
        self.mobile_ent.place(relx=0.335, rely=0.334, height=29, relwidth=0.293)
        self.test.trace_variable("w",self.input_validation)

        self.username_lbl_reg = Label(self.registration_frame,font= font10,bg='#6932a8',text="Username :")
        self.username_lbl_reg.place(relx=0.220, rely=0.456, height=27, width=90)

        self.username_ent_reg = Entry(self.registration_frame)
        self.username_ent_reg.place(relx=0.338, rely=0.456, height=29, relwidth=0.293)

        self.pass_lbl = Label(self.registration_frame,text ="Password :",bg="#6932a8",font=font10)
        self.pass_lbl.place(relx=0.214, rely=0.58, height=27, width=95)

        self.pass_ent = Entry(self.registration_frame,show='*')
        self.pass_ent.place(relx=0.338, rely=0.58, height=29, relwidth=0.293)

        self.pass_confirm_lbl = Label(self.registration_frame, bg="#6932a8", text="Confirm :", font=font10)
        self.pass_confirm_lbl.place(relx=0.21, rely=0.696, height=27, width=95)

        self.pass_confirm_ent = Entry(self.registration_frame,show = "*")
        self.pass_confirm_ent.place(relx=0.339, rely=0.696, height=29, relwidth=0.293)

        self.register_btn = Button(self.registration_frame, text="Register",
                                   command = self.registration_validation)
        self.register_btn.place(relx=0.383, rely=0.891, height=37, width=123)

        self.root.mainloop()

    def registration_validation(self):
        """
        Method which validates the info of user in registration and stores it if it is only correct.
        :return: None
        """
        a = self.name_ent.get()
        b = self.mobile_ent.get()
        c = self.username_ent_reg.get()
        d = self.pass_ent.get()
        e = self.pass_confirm_ent.get()
        blank = [a.replace(" ",""),b.replace(" ",""),c.replace(" ",""),d.replace(" ",""),
                 e.replace(" ","")]

        self.users = []
        if c.upper() in self.users:
            messagebox.showinfo("Error !","User already exist")
        elif "" in blank:
            messagebox.showerror("Error !","You must provide all the credentials")
        elif len(c) < 5 or len(c) > 15:
            messagebox.showerror("Error !", "Username must be between 5 - 15 in length.")
        elif len(d) < 8 or len(d) > 50:
            messagebox.showerror("Error !", "Password must be between 8 - 50 in length")
        elif d != e:
            messagebox.showerror("Error !", "Password do not match !")
        else:
            if self.indicator == 0:
                test = open("reg.txt","wb+")
                pickle.dump([],test)
            test = open("reg.txt", "rb+")
            data = pickle.load(test)
            file = {"name": a.upper(), "phone": b.upper(), "username": c.upper(), "password": d}
            data.append(file)
            write_file = open("reg.txt", "wb+")
            pickle.dump(data, write_file)
            write_file.close()
            messagebox.showinfo("Congratulations !", "Registration Successful !")
            self.registration_frame.place_forget()
            self.login_interface()

    def login_interface_1st(self):
        """
        Interface design when user got the correct credentials to log in !
        :return: None
        """
        self.loginpage_frame.place_forget()

        self.interface_1st_win_frame = Frame(self.mainframe,relief="groove",bg="#6932a8",bd=2)
        self.interface_1st_win_frame.place(relx=0.010, rely=0.150, relheight=0.830, relwidth=0.981)

        self.TSeparator1 = ttk.Separator(self.interface_1st_win_frame,orient ="vertical")
        self.TSeparator1.place(relx=0.238, rely=0.024, relheight=0.946)

        self.Frame3 = Frame(self.interface_1st_win_frame,bd = 2,relief = "groove",bg ="#ffffff")
        self.Frame3.place(relx=0.249, rely=0.026, relheight=0.948, relwidth=0.74)

        self.TButton1 = Button(self.interface_1st_win_frame,text = "Log out",command = self.log_out,bg = "black",
                               fg = "white")
        self.TButton1.place(relx=0.034, rely=0.518, height=30, width=98)



        self.Frame5 = Frame(self.interface_1st_win_frame,bg="#6932a8",bd="2",relief ="groove")
        self.Frame5.place(relx=0.01, rely=0.024, relheight=0.353, relwidth=0.22)
        self.Frame5.configure(background="#6932a8")

        self.TButton4 = Button(self.Frame5,text = "User Registration",command =self.registration,bg = "#6932a8")
        self.TButton4.place(relx=0.040, rely=0.058, height=40, width=158)

        self.TButton4_14 = Button(self.Frame5,text = "Remove Employee",command = self.remove,bg = "#6932a8")
        self.TButton4_14.place(relx=0.040, rely=0.381, height=40, width=158)

        self.TButton4_15 = Button(self.Frame5,text = "Registration",command =self.employee_registration,bg = "#6932a8")
        self.TButton4_15.place(relx=0.040, rely=0.697, height=40, width=158)
        self.scroll_x = Scrollbar(self.Frame3, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Frame3, orient=VERTICAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.student_table = ttk.Treeview(self.Frame3, column=('first_name', 'last_name', 'Department', 'Mobile', 'Email'),
                                          xscrollcommand=self.scroll_x.set,
                                          yscrollcommand=self.scroll_y.set)
        self.student_table.heading('first_name', text="Full Name")
        self.student_table.heading('last_name', text="Nationality")
        self.student_table.heading('Department', text="Department")
        self.student_table.heading('Mobile', text="Mobile")
        self.student_table.heading('Email', text="Email")
        self.student_table['show'] = 'headings'

        self.student_table.column('first_name', width=120)
        self.student_table.column('last_name', width=120)
        self.student_table.column('Department', width=120)
        self.student_table.column('Mobile', width=120)
        self.student_table.column('Email', width=120)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

        self.student_table.bind(('<ButtonRelease-1>'), self.pointer)
        self.student_table.pack(fill=BOTH, expand=True)
        self.show()
    def show(self):
        """
        Shows the data to Tree view !
        :return: None
        """
        try:
            query= open("Employee.txt","rb+")
            result = pickle.load(query)
            print(result)
        except Exception:
            query = open("Employee.txt","wb+")
            result = pickle.dump([],query)
            result = []


        self.student_table.delete(*self.student_table.get_children())
        for row in result:
                self.student_table.insert('',END,values= (row["first_name"],row["last_name"],row["Department"],
                                                          row["Mobile"],row["Email"]))

    def pointer(self,event):
        """
        Highlights the selected !
        :param event: Select the pointed part
        :return: None
        """
        try:
            point = self.student_table.focus()
            content = self.student_table.item(point)
            row = content['values']
            if len(row) != 0:
                point1 = row[3]
                self.pointed = [point1]
        except Exception:
            self.pointed = []

    def employee_registration(self):
        """
        Employee Registration , takes credentials from user to store !
        :return: None
        """
        try:
            a = open("Employee.txt","rb+")
            pickle.load(a)
        except Exception:
            test = []
            a = open("Employee.txt","wb+")
            pickle.dump(test,a)

        font9 = "-family {Segoe UI Black} -size 11 -weight bold -slant" \
                " roman -underline 0 -overstrike 0"
        self.interface_1st_win_frame.place_forget()
        self.Frame1 = Frame(self.mainframe,relief = "groove",bd = 2,bg ="#6932a8")
        self.Frame1.place(relx=0.008, rely=0.15, relheight=0.841
                , relwidth=0.982)

        self.Label1 = Label(self.Frame1,font = font9,text = "Employee Registration",bg="#6932a8")
        self.Label1.place(relx=0.027, rely=0.022, height=46, width=892)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.188, rely=0.182,height=34, relwidth=0.276)

        self.Entry1_1 = Entry(self.Frame1)
        self.Entry1_1.place(relx=0.661, rely=0.176,height=34, relwidth=0.276)

        self.Entry1_2 = Entry(self.Frame1)
        self.Entry1_2.place(relx=0.188, rely=0.44,height=34, relwidth=0.276)

        self.Label2 = Label(self.Frame1,text = "Full Name :", bg = "#6932a8")
        self.Label2.place(relx=0.041, rely=0.18, height=36, width=112)

        self.Label2_3 = Label(self.Frame1,bg="#6932a8",text="Nationality :")
        self.Label2_3.place(relx=0.497, rely=0.185, height=36, width=112)

        self.Label2_4 = Label(self.Frame1,text = "Address :",bg = "#6932a8")
        self.Label2_4.place(relx=0.045, rely=0.44, height=36, width=112)

        self.Label3_3 = Label(self.Frame1,text = "Company :",bg = "#6932a8")
        self.Label3_3.place(relx=0.49, rely=0.308, height=36, width=112)

        self.Entry123 = Entry(self.Frame1)
        self.Entry123.place(relx=0.662, rely=0.298,height=34, relwidth=0.267)

        self.Label3 = Label(self.Frame1,text = "Department : ",bg ="#6932a8")
        self.Label3.place(relx=0.044, rely=0.308, height=36, width=112)

        self.Label2_5 = Label(self.Frame1,bg ="#6932a8",text = "Mobile Number :")
        self.Label2_5.place(relx=0.516, rely=0.431, height=36, width=112)

        self.Entry1_4 = Entry(self.Frame1)
        self.Entry1_4.place(relx=0.662, rely=0.431,height=34, relwidth=0.276)

        self.Label2_5 = Label(self.Frame1,text = "Email :",bg="#6932a8")
        self.Label2_5.place(relx=0.209, rely=0.571, height=36, width=72)

        self.Entry1_5 = Entry(self.Frame1)
        self.Entry1_5.place(relx=0.293, rely=0.571,height=34, relwidth=0.402)

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.007, rely=0.831, relwidth=0.984)

        self.TButton1 = ttk.Button(self.Frame1,text ="Register",command=self.submit)
        self.TButton1.place(relx=0.408, rely=0.725, height=40, width=148)

        self.TButton13 = ttk.Button(self.Frame1,text = "Back",command =self.back_regem)
        self.TButton13.place(relx=0.008, rely=0.845, height=40, width=148)
        a = open("Employee.txt","rb+")
        b = pickle.load(a)
        list2 = []
        for i in b:
            if i["Department"] not in list2:
                list2.append(i["Department"])
        self.TCombobox1 = ttk.Combobox(self.Frame1,values = list2)
        self.TCombobox1.place(relx=0.188, rely=0.308, relheight=0.079
                , relwidth=0.28)
        if list2 != []:
            self.TCombobox1.set(list2[0])

    def submit(self):
        """
        Validation for employees data and storing data.
        :return: None
        """
        a = self.Entry1.get()
        b = self.Entry1_1.get()
        c = self.TCombobox1.get()
        e = self.Entry1_4.get()
        f = self.Entry1_5.get()
        test = open("Employee.txt", "rb+")
        data = pickle.load(test)
        list = [a.strip(), b.strip(), c.strip(), e.strip(), f.strip()]
        list3 = []
        for i in data:
            list3.append(i["Mobile"])
        if e in list3:
            messagebox.showerror("Error !","Employee Already Exists")
        elif "" in list:
            messagebox.showinfo("Error !","You can't left it blank !")
        elif "@" not in f.upper():
            messagebox.showinfo("Error !","Wrong Email !")
        else:
            test = open("Employee.txt", "rb+")
            data = pickle.load(test)
            file = {"first_name": a.upper(), "last_name": b.upper(), "Department": c.upper(), "Mobile": e,"Email":f.upper()}
            data.append(file)
            write_file = open("Employee.txt", "wb+")
            pickle.dump(data, write_file)
            write_file.close()
            messagebox.showinfo("Congratulations !", "Registration Successful !")
            self.back_regem()
            self.show()

    def input_validation(self,*args):
        """
        validates the input by only allowing integer as response on entry.
        :return None
        """
        a = self.test.get()
        try:
            b = int(a)
            if b > 9999999999:
                self.test.set(a[:-1])
        except Exception:
            self.test.set(a[:-1])

    def log_out(self):
        """
        getting back to login interface
        :return: None
        """
        self.login_interface()

    def back_reg(self):
        """
        getting back to login interface from user registration
        :return: None
        """
        self.registration_frame.place_forget()
        self.login_interface_1st()

    def back_regem(self):
        """"
        Getting back to login interface from employee registration
        :return None
        """
        self.Frame1.place_forget()
        self.login_interface_1st()

    def remove(self):
        """
        Removes employee from file and from tree view.
        :return: None
        """
        if self.pointed == []:
            messagebox.showerror("Error !","Please select an Employee to remove")
        else:
            load = open("Employee.txt","rb+")
            result = pickle.load(load)
            final = []
            print()
            print(self.pointed)
            for i in result:
                print(i["Mobile"])
                if str(i["Mobile"])== str(self.pointed[0]):
                    print("Removed")
                else:
                    final.append(i)
            print(final)
            if final == []:
                self.student_table.delete(*self.student_table.get_children())
            final_load = open("Employee.txt","wb+")
            pickle.dump(final,final_load)
            messagebox.showinfo("Successful !","Employee removed successfully")
            self.show()

a = Employee_management_system()