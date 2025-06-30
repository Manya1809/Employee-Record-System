from customtkinter import *
from PIL import Image
from tkinter import messagebox


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror("Error","All Fields are required")
    elif usernameEntry.get()=="Manya" and passwordEntry.get()=='1234':
        messagebox.showinfo("Success","Login is Succesfull")
        root.destroy()

    else:
        messagebox.showerror("Error","Invalid Credentials")


root=CTk()
root.geometry("930x487")
root.resizable(0,0)
root.title('login page')
image = CTkImage(Image.open('../images/employee.png'), size=(930, 478))
imageLabel = CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headingLabel = CTkLabel(root,text="Employee Information System",bg_color='#BCE4E6',font=("Goudy Old Style",22,'bold'),text_color="black")
headingLabel.place(x=350,y=60)

usernameEntry = CTkEntry(root,placeholder_text="Enter Your Username",width=190)
usernameEntry.place(x=380,y=120)

passwordEntry = CTkEntry(root,placeholder_text="Enter Your Password",width=190,show="*")
passwordEntry.place(x=380,y=160)

loginButton = CTkButton(root,text="Login",cursor="hand2",command=login)
loginButton.place(x=400,y=200)



root.mainloop()