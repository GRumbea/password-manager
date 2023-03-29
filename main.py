from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ------------------------------ PASSWORD GENERATOR ------------------------------ #
lwrcase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
uprcase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    pwd_lwr_case_letters = [choice(lwrcase_letters) for _ in range(randint(8, 10))]
    pwd_upr_case_letters = [choice(uprcase_letters) for _ in range(randint(4, 6))]
    pwd_nums = [choice(numbers) for _ in range(randint(4, 6))]
    pwd_symbols = [choice(symbols) for _ in range(randint(4, 6))]
    password_list = pwd_lwr_case_letters + pwd_upr_case_letters + pwd_nums + pwd_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ------------------------------ SAVE PASSWORD ------------------------------ #


def save():

    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Don't leave any fields empty.")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"""
        These are the details entered:\n
        Email/Username: {email_username}\n 
        Password: {password}\n 
        Is it okay to save?""")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email_username} | {password}\n")
                website_input.delete(0, END)
                email_username_input.delete(0, END)
                password_input.delete(0, END)


# ------------------------------ UI SETUP ------------------------------ #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1, sticky='e')

website_input = Entry(width=53)
website_input.grid(column=1, row=1, columnspan=2, sticky='w')
website_input.focus()

email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(column=0, row=2, sticky='e')

email_username_input = Entry(width=53)
email_username_input.grid(column=1, row=2, columnspan=2, sticky='w')

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3, sticky='e')

password_input = Entry(width=35)
password_input.grid(column=1, row=3, sticky='w')

generate_pass_btn = Button(text="Generate Password", command=generate_password)
generate_pass_btn.grid(column=2, row=3, sticky='w')

add_btn = Button(text="Add", width=45, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
