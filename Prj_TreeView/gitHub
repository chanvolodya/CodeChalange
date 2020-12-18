from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("MANAGEMENT")
root.geometry("600x600")

#=======Variables=============
userName = StringVar()
userId =StringVar()
userProduct =StringVar()
data = []
#=======Function==============
def clear():
    userName.set("")
    userId.set("")
    userProduct.set("")
    

def addData():
    global data
    name = userName.get()
    Id = userId.get()
    product =userProduct.get()
    if(name!="" and Id!="" and product!=""):
        try:
            user=[name,Id,product]
            data.append(user)
            clear()
            messagebox.showinfo(title="Infor",message="Success added")  
        except ValueError:
            messagebox.showinfo(title="Infor",message="Empty content")
#         for item in data:
#             print(item)
        
def showData():
    global data
    clearData()
    count =0
    for item in data:
        my_tree.insert(parent="",index="end",iid=count,values=(item[0],item[1],item[2]))
        count+=1

def clearData():
    for item in my_tree.get_children():
        my_tree.delete(item)
        
def deleteData():
    global data
    x = my_tree.selection()
    print(x)
    for record in x:
        del(data[int(record)])
        my_tree.delete(record)
        

def updateData():
    global data
    x = my_tree.selection()[0]
    print(x)
    for record in x:
        data_selected = data[int(record)]
        userName.set(data_selected[0])
        userId.set(data_selected[1])
        userProduct.set(data_selected[2])
        print(data[int(record)])
#        my_tree.delete(record)

#=======Designer==============
lblName = Label(root,text = "Имя пользователя").grid(row =0, column =0,padx=5,pady=5,sticky = W)
txtName =Entry(root,textvariable =userName).grid(row =0, column =1,padx=5,pady=5)
lblId = Label(root,text = "Индентификация").grid(row =1, column =0,padx=5,pady=5,sticky = W)
txtId =Entry(root,textvariable =userId).grid(row =1, column =1,padx=5,pady=5)
lblProduct = Label(root,text = "Продук").grid(row =2, column =0,sticky = W,padx=5,pady=5)
txtProduct =Entry(root,textvariable =userProduct).grid(row =2, column =1)

btnAdd = Button(root,text ="Добавить в список",command =addData).grid(row =3, column =0,sticky = W,padx=5,pady=5)
btnDel = Button(root,text ="Удалить список",command =deleteData).grid(row =3, column =1,sticky = W,padx=5,pady=5)
btnUpdate = Button(root,text ="Обновить список",command =updateData).grid(row =3, column =2,sticky = W,padx=5,pady=5)
btnShow = Button(root,text ="Cписок",command =showData).grid(row =4, columnspan=2,sticky = W,padx=5,pady=5)
btnShow = Button(root,text ="Close",command =lambda: root.destroy()).grid(row =4, column=2,sticky = W,padx=5,pady=5)
my_tree = ttk.Treeview(root)

#Define columns
my_tree['columns']= ("Name","ID","Product")

#custom column

my_tree.column("#0",width=0, minwidth=25,stretch=NO)
my_tree.column("Name",width=180, minwidth=25)
my_tree.column("ID",width=150, minwidth=25)
my_tree.column("Product",width=170, minwidth=25)

my_tree.heading("#0",text="Label",anchor =W)
my_tree.heading("Name",text="Имя пользователя",anchor =CENTER)
my_tree.heading("ID",text="Индентификация",anchor =CENTER)
my_tree.heading("Product",text="Продук",anchor =CENTER)


my_tree.grid(rowspan =7, columnspan=7)



root.mainloop()