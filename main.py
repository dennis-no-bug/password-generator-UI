from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json

#Password Generator

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


def add_data():
    user_password = password_input.get()
    user_website = website_input.get()
    user_email = email_input.get()
    new_data = {
        user_website: {
            "email": user_email,
            "password": user_password,
        }
    }

    if len(user_website) == 0 or len(user_email) == 0 or len(user_password) == 0:
        messagebox.showwarning(title="Password Manager", message="Please do not left any field empty!")

    else:
        try:
            with open("Saved_user_data.json", mode="r") as user_data:
                # Reading old data
                data = json.load(user_data)

        except FileNotFoundError:
            with open("Saved_user_data.json", mode="w") as user_data:
                # Saving updated data
                json.dump(new_data, user_data, indent=4)

        else:
            data.update(new_data)

            with open("Saved_user_data.json", mode="w") as user_data:
                json.dump(data, user_data, indent=4)

        finally:
            password_input.delete(0, END)
            website_input.delete(0, END)
            email_input.delete(0, END)

        messagebox.showinfo(title="Password Manager", message="Your password has been successfully saved.")

def find_password():
    user_website = website_input.get()
    try:
        with open("Saved_user_data.json", mode="r") as user_data:
            data = json.load(user_data)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found!")

    else:
        if user_website in data:
            email = data[user_website]["email"]
            password = data[user_website]["password"]
            messagebox.showinfo(title=user_website, message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showerror(title="Error", message=f"There is no data saved for <{user_website}>.  ")



#User Interface
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry
website_input = Entry(width=33)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=1)

email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=33)
password_input.grid(row=3, column=1)

#Button
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
