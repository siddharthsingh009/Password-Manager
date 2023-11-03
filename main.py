from tkinter import *
from tkinter import messagebox
import random
import string
import json

black = "black"
white = "white"
font = ("Argent", 10, "bold")
email = "xyz@example.com"


def generate_password():
    """Generates a randomly chosen password and fills it in the password entry box"""
    alphabets = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    all_string = alphabets + numbers + symbols
    password = ''
    for _ in range(12):
        password += random.choice(all_string)

    password_entry.insert(0, password)


def saving_password():
    """ Saves all the details in JSON format everytime user generates or creates a password and clicks on save
    password button"""
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    data_dict = {website: {
        'email': username,
        'password': password,
        }
    }

    if len(username) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showerror(title='Error', message='All or some fields are empty. Please do not leave any '
                                                    'field/s empty')
    else:
        is_ok = messagebox.askyesno(title="Warning", message="Do you want to save password ?")

        if is_ok:
            try:
                with open("passwords.json", "r") as data_file:
                    data = json.load(data_file)  # reads already existing data
            except FileNotFoundError:
                with open('passwords.json', "w") as write_file:
                    json.dump(data_dict, write_file, indent=4)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
            else:
                data.update(data_dict)  # updates new_dict with newly received data
                with open('passwords.json', "w") as write_file:
                    json.dump(data, write_file, indent=4)  # writes on the file
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def searching_data():
    """Searches and displays the data related to the website enetered by user."""
    website = website_entry.get()
    try:
        with open('passwords.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f'{website}', message=f'There is no information available related to {website}.')
    except KeyError:
        messagebox.showinfo(title=f'{website}', message=f'There is no information available related to {website}.')
    else:
        emailid = data[website]['email']
        password = data[website]['password']
        messagebox.showinfo(title=f'{website}', message=f'Email: {emailid}\n\n Password: {password}')


# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="black")

# Integrating the logo Image
canvas = Canvas(height=200, width=200, bg="black", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1, columnspan=2)

# Labels
website_label = Label(text="Website:", bg="black", font=font, fg=white)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="black", font=font, fg=white)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="black", font=font, fg=white)
password_label.grid(row=3, column=0)

# Text Boxes
website_entry = Entry(width=25, font=('Argent', 12, 'normal'))
website_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
website_entry.focus()

email_entry = Entry(width=25, font=('Argent', 12, 'normal'))
email_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
email_entry.insert(index=0, string=email)

password_entry = Entry(width=25, font=('Argent', 12, 'normal'))
password_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

# Blank Line
blank_line_2 = Label(bg=black)
blank_line_2.grid(row=4, column=1)


# Buttons
search_button = Button(text="Search", width=20, bg=white, font=font, fg=black, command=searching_data)
search_button.grid(row=1, column=5)

generate_password_button = Button(text="Generate Password", width=20, bg=white, font=font, fg=black, command=generate_password)
generate_password_button.grid(row=3, column=5)

save_button = Button(text="Save Password", width=30, bg=white, font=font, fg=black, command=saving_password)
save_button.grid(row=6, column=1, columnspan=2)


# The mainloop prevents the screen from disappearing
window.mainloop()
