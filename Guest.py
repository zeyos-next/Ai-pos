from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox as pop_up
import random
import AccountSystem

import customtkinter as ctk
class GuestPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = ctk.CTk()

        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        # window Icon
        icon = PhotoImage(file=r'./images/logo.png')
        dashboard_window.iconphoto(True, icon)
        dashboard_window.title('Welcome')

        # Navigating through windows
        homepage = Frame(dashboard_window)
        dashboard_page = Frame(dashboard_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')


        def show_frame(frame):
            frame.tkraise()


        show_frame(homepage)

        # ======================================================================================
        # =================== HOME PAGE ========================================================
        # ======================================================================================
        homepage.config(background='#ffffff')

        # ====== MENU BAR ==========
        logoIcon = Image.open('images\\logo.png')
        logoIcon = logoIcon.resize((50,50))
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(homepage, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(relx=0.5, y=0)


        menuBar_line = Canvas(homepage, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
        menuBar_line.place(x=0, y=60)


        def update_background():
                
                # Get window size
                window_width = homepage.winfo_width()
                window_height = homepage.winfo_height()

                # Open and resize the image to match the window size
                home_bgImg = Image.open('images\\home.jpg')
                home_bgImg = home_bgImg.resize((window_width, window_height))

                # Update the photo
                photo = ImageTk.PhotoImage(home_bgImg)

                # Update the Label with the resized image
                home_bg.config(image=photo)
                home_bg.image = photo

        # Create the Label
        home_bgImg = Image.open('images\\home.jpg')
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(x=0, y=60)

            # Bind the update to window resizing
        homepage.bind('<Configure>', lambda e: update_background())

        def click_button():
            pop_up.showinfo(" Ooops ! !! !!!", 'For you to gain access to the full functionality of this App\n'
                            'You will need an Administrator Approval\n\n'
                            'Please inform your Administrator for full usage approval')

        # ========== HOME BUTTON =======
        home_button = Button(homepage, text='Home', bg='#6DA3C0', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#6DA3C0', activeforeground='white')
        home_button.place(x=70, y=15)

        # ========== DASHBOARD BUTTON =======
        dashboard_button = Button(homepage, text='Dashboard', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                  cursor='hand2', activebackground='#6DA3C0', activeforeground='#7a7a7a',
                                  command=click_button)
        dashboard_button.place(x=150, y=15)

        # ========== MANAGE BUTTON =======
        manage_button = Button(homepage, text='Manage', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#6DA3C0', activeforeground='#7a7a7a',
                               command=click_button)
        manage_button.place(x=270, y=15)

        # ========== PRODUCTS BUTTON =======
        product_button = Button(homepage, text='Products', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                cursor='hand2', activebackground='#6DA3C0', activeforeground='#7a7a7a',
                                command=click_button)
        product_button.place(x=360, y=15)

        # ========== HELP BUTTON =======
        help_button = Button(homepage, text='Help', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                             cursor='hand2', activebackground='#6DA3C0', activeforeground='#7a7a7a',
                             command=click_button)
        help_button.place(x=460, y=15)

        def logout():
            win = Toplevel()
            AccountSystem.AccountPage(win)
            dashboard_window.withdraw()
            win.deiconify()
        # ========== LOG OUT =======
        logout_button = Button(homepage, text='Logout', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#6DA3C0', activeforeground='#7a7a7a', command=logout)
        logout_button.place(x=520, y=15)

        admLabel =ctk.CTkLabel(homepage, text='GUEST', font=('yu gothic ui', 18, 'bold'), fg_color="white",text_color="black")
        admLabel.place(relx=0.9, y=11)

        frame = ctk.CTkFrame(homepage, corner_radius=15, fg_color="#000",bg_color="transparent")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add the label inside the frame with internal padding
        heading = ctk.CTkLabel(frame, text='Welcome to \nZeyos POS', font=("yu gothic ui", 25, "bold"), text_color="white",bg_color="transparent")
        heading.pack(padx=30, pady=10)



def page():
    window = Tk()
    GuestPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
