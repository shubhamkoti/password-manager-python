
from tkinter import *
from tkinter import messagebox
from random import choice , randint,shuffle
import  pyperclip

"""PASSWORD GENERATOR"""
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '?']

    password_letters=[choice(letters) for _ in range(randint(8,10))]
    password_symbol=[choice(symbols) for _ in range(randint(2,4))]
    password_numbers=[choice(numbers) for _ in range(randint(2,4))]

    password_list=password_numbers+password_symbol+password_letters
    shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)
    #
    # password_list = []
    #
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list.append(random.choice(symbols))
    #
    # for char in range(nr_numbers):
    #     password_list.append(random.choice(numbers))
    #
    # random.shuffle(password_list)
    #
    # password=""
    # for char in password_list:
    #     password += char
    # print(f"Your Password is: {password}")

""" Saving sata in file   SAVE PASSWORD """
def save_data():
    website_data=website_entry.get()
    email_data=email_entry.get()
    password_data=password_entry.get()
    if website_data=="" or email_data=="" or password_data=="":
        messagebox.showerror(title="Opps",message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title="Message",message=f"These are the details entered: \nEmail: {email_data}"
         f"\nPassword: {password_data} \nIs it ok to Save?")

    if is_ok:
     with open("data.txt","a")as file:
        file.write(f"{website_data} | {email_data} | {password_data}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)


"""UI SetUP"""
window=Tk()
# window.config(bg="red")
window.config(pady=20,padx=20)
window.grid_columnconfigure(0, minsize=120)
window.grid_columnconfigure(1, minsize=250)
window.title("Password Manager")
# window.config(bg="pink")

mypass=PhotoImage(file="img.png")
canvas=Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,80,image=mypass)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0,sticky='e', padx=5, pady=5,)
email_Label=Label(text="Email/Username:")
email_Label.grid(row=2,column=0,sticky='e', padx=5, pady=5,)
password_label=Label(text="Password")
password_label.grid(row=3,column=0,sticky='e', padx=5, pady=5,)


# Entries
website_entry=Entry(width=40)
website_entry.grid(row=1,column=1,columnspan=2,sticky='w', padx=5, pady=5,)
website_entry.focus()

email_entry=Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2,sticky='w', padx=5, pady=5,)
email_entry.insert(0,"Shubhamkoti89@gmail.com")
password_frame = Frame(window)
password_frame.grid(row=3, column=1, columnspan=2)

password_entry = Entry(password_frame, width=21)
password_entry.pack(side="left")

generate_password_button = Button(
    password_frame,
    text="Generate Password",
    command=generate_password
)
generate_password_button.pack(side="left", padx=2)
add_button=Button(text="Add", width=36, command=save_data)
add_button.grid(row=4,column=1,columnspan=2)


window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(5, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(3, weight=1)
window.mainloop()
