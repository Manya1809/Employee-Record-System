from customtkinter import *
from PIL import Image
from tkinter import ttk , messagebox
from files import database


#============functions==========

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchbox.set("Search By")
def search_employee():
    if searchEntry.get()=="":
        messagebox.showerror("Error","Enter value to Search")
    elif searchbox.get()=="Search By":
        messagebox.showerror("Error","Please select some option")
    else:
        searched_data= database.search(searchbox.get(), searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)
def delete_all():
    result=messagebox.askyesno('Confirm',"Do you really want to delete all records?")
    if result:
        database.deleteall_records()

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select Data to Delete")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror("Error", "Data is Deleted")


def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select Data to Update")
    else:
        database.update(idEntry.get(), nameEntry.get(), phEntry.get(), rolebox.get(), genderbox.get(), salEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success',"Data is updated")

def selection(event):
    selected_item =tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0, row[1])
        phEntry.insert(0, row[2])
        rolebox.set( row[3])
        genderbox.set(row[4])
        salEntry.insert(0,row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    phEntry.delete(0, END)
    salEntry.delete(0, END)
    nameEntry.delete(0, END)
def treeview_data():
    employees= database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)

def add_employee():
    if idEntry.get()=='' or phEntry.get()=='' or nameEntry.get()=='' or salEntry.get()=='' :
        messagebox.showerror("Error","All Fields are Required")
    elif database.id_exists(idEntry.get()):
        messagebox.showerror("Error","Id Already Exists")
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error',"Invalid ID format Use 'EMP' followed by a number (e.g. , 'EMP1).")


    else:
        database.insert(idEntry.get(), nameEntry.get(), phEntry.get(), rolebox.get(), genderbox.get(), salEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data has been added succesfully.")

#=============GUI PART======================
window=CTk()
window.geometry("1000x580+100+100")
window.resizable(0,0)
window.title('Employee Information System')
window.configure(fg_color="#161C30")
logo= CTkImage(Image.open('../images/employee.png'), size=(1000, 158))
logolabel=CTkLabel(window,image=logo,text="")
logolabel.grid(row=0,column=0,columnspan=2)

leftFrame = CTkFrame(window,fg_color="#161C30")
leftFrame.grid(row=1,column=0)

idLabel = CTkLabel(leftFrame,text='Id',font=('arial',18,"bold"),text_color="white")
idLabel.grid(row=0,column=0,padx=20)
idEntry = CTkEntry(leftFrame,font=('arial',15,"bold"),width=180)
idEntry.grid(row=0,column=1,pady=15,sticky=W)

nameLabel = CTkLabel(leftFrame,text='Name',text_color="white",font=('arial',18,"bold"))
nameLabel.grid(row=1,column=0,padx=20)
nameEntry = CTkEntry(leftFrame,font=('arial',15,"bold"),width=180)
nameEntry.grid(row=1,column=1,pady=15,sticky=W)

phLabel = CTkLabel(leftFrame,text='Phone',text_color="white",font=('arial',18,"bold"))
phLabel.grid(row=2,column=0,padx=20)
phEntry = CTkEntry(leftFrame,font=('arial',15,"bold"),width=180)
phEntry.grid(row=2,column=1)

roleLabel = CTkLabel(leftFrame,text='Role',text_color="white",font=('arial',18,"bold"))
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky=W)
role_options=['Web Developer','Cloud Architect','Technical Writer','Network Engineer',
              'Data Scientist','Bussiness Analyst','IT Consultant','UI/UX Designer']
rolebox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state="readonly")
rolebox.grid(row=3,column=1)
rolebox.set(role_options[0])

genderLabel = CTkLabel(leftFrame,text='Gender',text_color="white",font=('arial',18,"bold"))
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky=W)
gender_options=['Male','Female']
genderbox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',15,'bold'),state="readonly")
genderbox.grid(row=4,column=1)
genderbox.set(gender_options[0])
salLabel = CTkLabel(leftFrame,text='Salary',text_color="white",font=('arial',18,"bold"))
salLabel.grid(row=5,column=0,padx=20)
salEntry = CTkEntry(leftFrame,font=('arial',15,"bold"),width=180)
salEntry.grid(row=5,column=1)

rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1,sticky=W,columnspan=3)

search_options=['Id','Name','Role','Phone','Gender','Salary']
searchbox=CTkComboBox(rightFrame,values=search_options,state="readonly")
searchbox.grid(row=0,column=0)
searchbox.set('Search By')

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)
searchButton = CTkButton(rightFrame,width=100,text='Search',command = search_employee)
searchButton.grid(row=0,column=2)
showallButton = CTkButton(rightFrame,width=100,text='Show All',command=show_all)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)
tree['columns']=('Id','Name','Phone','Role','Gender','Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=80)
tree.column('Name',width=120)
tree.column('Phone',width=140)
tree.column('Role',width=160)
tree.column('Gender',width=80)
tree.column('Salary',width=90)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',15,'bold'))
style.configure('Treeview',font=('arial',12,'bold'),rowheight=20,background='#161c30',foreground = "white")
scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,stick='ns')
tree.config(yscrollcommand=scrollbar.set)


buttonFrame=CTkFrame(window,fg_color="#161C30")
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonFrame,text="New Employee",font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text="Add Employee",font=('arial',15,'bold'),width=160,corner_radius=15,command= add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)
updateButton=CTkButton(buttonFrame,text="Update Employee",font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)
deleteButton=CTkButton(buttonFrame,text="Delete Employee",font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)
deleteallButton=CTkButton(buttonFrame,text="Delete All",font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()
window.bind('<ButtonRelease>',selection)
window.mainloop()