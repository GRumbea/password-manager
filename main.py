from tkinter import *

# ------------------------------ PASSWORD MANAGER ------------------------------ #

# ------------------------------ SAVE PASSWORD ------------------------------ #

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

email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(column=0, row=2, sticky='e')

email_username_input = Entry(width=53)
email_username_input.grid(column=1, row=2, columnspan=2, sticky='w')

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3, sticky='e')

password_input = Entry(width=35)
password_input.grid(column=1, row=3, sticky='w')

generate_pass_btn = Button(text="Generate Password")
generate_pass_btn.grid(column=2, row=3, sticky='w')

add_btn = Button(text="Add", width=45)
add_btn.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
