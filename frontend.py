from tkinter import *

import backend_sc3

def get_selected_row(event):
        global selected_tuple
        index = listbox1.curselection()[0]
        selected_tuple = listbox1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])



def view_command():
        listbox1.delete(0,END)
        for row in backend_sc3.view():
                listbox1.insert(END,row)

def search_command():
        listbox1.delete(0,END)
        for row in backend_sc3.search(name_val.get(),enrol_val.get(),roll_val.get(),cont_val.get()):
                listbox1.insert(END,row)

def add_command():
        backend_sc3.insert(name_val.get(),enrol_val.get(),roll_val.get(),cont_val.get())
        listbox1.delete(0,END)
        listbox1.insert(END,(name_val.get(),enrol_val.get(),roll_val.get(),cont_val.get()))

def delete_command():
        backend_sc3.delete(selected_tuple[0])

def update_command():
        backend_sc3.update(selected_tuple[0],name_val.get(),enrol_val.get(),roll_val.get(),cont_val.get())

window = Tk()
window.wm_title("Student's Portal")


l1 = Label(window,text = "Name")
l1.grid(row = 0, column = 0)

l1 = Label(window,text = "Enrollment ID")
l1.grid(row = 0, column = 2)

l1 = Label(window,text = "Roll No.")
l1.grid(row = 1, column = 0)

l1 = Label(window,text = "Contact")
l1.grid(row = 1, column = 2)

name_val = StringVar()
e1 = Entry(window,textvariable = name_val)
e1.grid(row = 0,column = 1)

enrol_val = StringVar()
e2 = Entry(window,textvariable = enrol_val)
e2.grid(row = 0,column = 3)

roll_val = StringVar()
e3 = Entry(window,textvariable = roll_val)
e3.grid(row = 1,column = 1)

cont_val = StringVar()
e4 = Entry(window,textvariable = cont_val)
e4.grid(row = 1,column = 3)

listbox1 = Listbox(window,height = 6,width = 35)
listbox1.grid(row = 2,column = 0,rowspan = 6,columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2,column = 2,rowspan = 6)

listbox1.configure(yscrollcommand = sb1.set)
sb1.configure(command = listbox1.yview)

listbox1.bind('<<ListboxSelect>>',get_selected_row)


b1 = Button(window,text = "View All", width = 12,command = view_command)
b1.grid(row = 2,column = 3)

b1 = Button(window,text = "Search",width = 12,command = search_command)
b1.grid(row = 3,column = 3)

b1 = Button(window,text = "Add Entry", width = 12,command = add_command)
b1.grid(row = 4,column = 3)

b1 = Button(window,text = "Update", width = 12,command = update_command)
b1.grid(row = 5,column = 3)

b1 = Button(window,text = "Delete", width = 12,command = delete_command)
b1.grid(row = 6,column = 3)

b1 = Button(window,text = "Close",width = 12,command = window.destroy)
b1.grid(row = 7,column = 3)

window.mainloop()
























































































