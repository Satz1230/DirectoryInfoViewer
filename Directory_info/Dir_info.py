# Script to get the Info of a directory
import os
from tkinter import *
from tkinter import messagebox
# global variable

info = dict(path="",files=0,folders=0, links=0,size=0)
# To get User-Input
def user_input():
     global info
     info['path'] = ""
     info['files'] = 0
     info['folders'] = 0
     info['links'] = 0
     info['size'] = 0

     enter_value = enter.get()

     rt = os.path.abspath(enter_value)


     if not os.path.exists(rt):
          x=messagebox.askretrycancel(title="Wrong Input",message=f"The Entered Path: {info['path']} doesn't exist!",icon='info')
          if not x:
                   quit(1)

     if not os.path.isdir(rt):
          y=messagebox.askretrycancel(title="Wrong Input", message=f"The Entered Path: {info['path']} isn't a directory!",icon='info')
          if not y:
              quit(2)


     info['path'] = rt

# Scan the path recursively
def scan(path):
     global info
     scan_t.set(f"------Scanning------ \n{info['path']}")

     for root,dirs,files in os.walk(path,onerror=None,followlinks=False):
          info['folders'] += len(dirs)
          info['files'] += len(files)
          for name in files:
               rootname = os.path.join(root, name)
               size = os.path.getsize(rootname)
               info['size'] += size

# Display
def display():
     global info
     result_t.set("------Results------")
     path_l.config(text=f"Path: {info['path']}")
     folders_l.config(text=f"Folders: {info['folders']}")
     files_l.config(text=f"Files: {info['files']}")
     links_l.config(text=f"Links: {info['links']}")
     size_l.config(text=f"------Size------"
                        f"\n{info['size']/1000} Kilobytes(kB)"
                        f"\n{info['size']/1e+6} Megabytes(MB)"
                        f"\n{info['size']/1e+9} Gigabytes(GB)")

# Main
def main():
     global info
     user_input()
     scan(info['path'])
     display()

def mainb(event):
     global info
     user_input()
     scan(info['path'])
     display()

window = Tk()

window.title("Directory Info")
window.resizable(False, False)
window.iconphoto(True, PhotoImage(file='media file/iconphoto.png'))
# Main Frame...................................................
frame= Frame(window)
frame.pack()

# Functioning Frame...............................................

frame1 = Frame(frame)
frame1.grid(row=0,column=0)

label1 = Label(frame1,text="Enter a Folder Path:",font=("consolas",15))
label1.grid(row=0,column=0,sticky='nw')

enter = Entry(frame1,width=30)
enter.grid(row=0,column=1,sticky='ne',pady=6)

info_button = Button(frame1,text="Get info!",font=("consolas",),command=main)
info_button.grid(row=1,column=1,sticky='ne')

# Info Frame...............................................

frame2 = Frame(frame)
frame2.grid(row=1,column=0)

scan_t = StringVar()
result_t = StringVar()

label3 = Label(frame2,textvariable=scan_t,font=("consolas",14))
label3.grid(row=0,column=0,sticky='nw')

label4 = Label(frame2,textvariable=result_t,font=("consolas",14))
label4.grid(row=1,column=0,sticky='nw')

# Info labels...............................................

FONT = ("Consolas",10)
GRID = dict(columnspan=1,sticky='nw')
path_l = Label(frame2,text='',font=FONT)
path_l.grid(row=2,**GRID)

folders_l = Label(frame2,text='',font=FONT)
folders_l.grid(row=3,**GRID)

files_l = Label(frame2,text='',font=FONT)
files_l.grid(row=4,**GRID)


links_l = Label(frame2,text='',font=FONT)
links_l.grid(row=5,**GRID)

size_l = Label(frame2,text='',font=FONT)
size_l.grid(row=6,**GRID)

# key bind.................................................

window.bind('<Return>',func=mainb)

# To open window in center of the screen.......................

frame_width = 450
frame_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2)-(frame_width/2))
y = int((screen_height/2)-(frame_height/2))

window.geometry(f"{frame_width}x{frame_height}+{x}+{y}")


window.mainloop()

