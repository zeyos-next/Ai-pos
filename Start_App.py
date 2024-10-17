from tkinter import *
from tkinter.ttk import Progressbar
import sys
import AccountSystem
import os
import customtkinter as ctk

from PIL import Image

root = ctk.CTk()
# root.resizable(0, 0)
# image = Image.Image('./images/coffeeShop-ico.png')

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
#root.wm_attributes('-alpha', 0.9)
root.wm_attributes('-topmost', True)
root.config(background='white')

welcome_label = ctk.CTkLabel(root,text='ZEYOS POS', font=("Poppins-Bold", 20, "bold"),text_color="black",fg_color="white")
welcome_label.place(relx=.5, y=35,anchor="center")
logoIcon = Image.open("images\\slogo.jpg")
ctk_image = ctk.CTkImage(logoIcon,size=(200,200))
bg_label = ctk.CTkLabel(root, image=ctk_image,text="",bg_color="white",width=500)
bg_label.place(relx = .03, rely = 0.2)

progress_label = ctk.CTkLabel(root, text="Please Wait...", font=('Poppins-SemiBold', 13, 'bold'),text_color="black",fg_color="white")
progress = ctk.CTkProgressBar(
    root,
    orientation="horizontal",
    determinate_speed=5,
    indeterminate_speed=5,
    mode="determinate",
    width=500,
    height=20,
    border_color="white",  # Make the outline color same as background to hide it
    border_width=0,        # Set border width to 0 to avoid any outline
    corner_radius=10,      # Rounded corners for both the bar and frame
    fg_color="black",      # Color of the progress fill
    bg_color="white"       # Ensure background blends smoothly
)



progress.step()
progress.place(x=15, y=390)
exit_btn = ctk.CTkButton(root,text='x',  command=lambda: exit_window(),fg_color="black",bg_color="white",width=45,font=('Poppins-SemiBold', 16, 'bold'))
exit_btn.place(relx = 0.92, y=-2)


def exit_window():
    sys.exit(root.destroy())


# def top():
#     root.withdraw()
#     os.system("python AccountSystem.py")
#     root.destroy()


i = 0
# Function to simulate progress
def load():
    global i
    if i <= 10:
        txt = 'Please Wait...  ' + (str(10 * i) + '%')
        progress_label.configure(text=txt)
        progress.set(i / 10)  # Update progress bar (i / 10 gives values from 0.0 to 1.0)
        progress_label.after(1000, load)  # Call `load` again after 1 second
        i += 1
    else:
        top()

# Dummy function to be called when progress is complete
def top():
    root.withdraw()
    os.system(r"python.exe AccountSystem.py")
    root.destroy()

# Start the loading process
load()
root.mainloop()
