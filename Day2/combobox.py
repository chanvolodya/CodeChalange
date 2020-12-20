from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Day 2 combobox")
root.geometry("450x450")

#==================Vaiables======================
IdKhoa= StringVar()
numberSv = StringVar()
tenKhoa= StringVar()
n= StringVar()
#==================Function======================
def Display():
    pass

def addTenKhoa():
    pass


#====================Gui=========================



txTenkhoa = Entry(root,textvariable = tenKhoa).pack(padx =5, pady=5)
btnTenKhoa = Button(root,text = "Them ten khoa vao combobox",command = addTenKhoa).pack(padx =5, pady=5)
lblTenKhoa = Label(root,text = "Ten khoa ").pack(padx =5, pady=5)
cbboxTenKhoa = ttk.Combobox(root,width =30,textvariable = n)
cbboxTenKhoa['values']=('Toan',
                         'Li',
                         'Hoa',
                         'Sinh')
cbboxTenKhoa.current()
cbboxTenKhoa.pack(padx =5, pady=5)


lblIdKhoa = Label(root,text= "Id cua khoa ").pack(padx =5, pady=5)
txtIdKhoa = Entry(root,textvariable = IdKhoa).pack(padx =5, pady=5)
lblSoSinhVien = Label(root,text= "So sinh vien cua khoa ").pack(padx =5, pady=5)
txtSoSinhVien = Entry(root,textvariable = numberSv).pack(padx =5, pady=5)

lblDisplay = Label(root,text = "Show here").pack(padx =5, pady=5)
btnDisplay = Button(root,text= "Show detail",command = Display).pack(padx =5, pady=5)



root.mainloop()