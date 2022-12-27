from tkinter import *

array = [4,2,123,15,3,1,12,23]

def sort():
    sorted_list = array
    sorted_list.sort()
    lbl_name = Label(text=array)
    lbl_name.pack()

root = Tk()
root.title('СОРТИРОВКА')
root.geometry('512x512')
arr_label = Label(text=array)
arr_label.pack()
button = Button(text='ОТСОРТИРОВАТЬ', command=sort)
button.pack()
root.mainloop()