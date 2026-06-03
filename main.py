import json
from tkinter import *
from tkinter import messagebox
from random import choice , randint,shuffle
import  pyperclip
import json

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
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

""" Saving sata in file   SAVE PASSWORD """
def save_data():
    website_data=website_entry.get().title()
    email_data=email_entry.get()
    password_data=password_entry.get()

    new_data={
        website_data:{
            "email":email_data,
            "password":password_data
        }
    }
    if website_data=="" or email_data=="" or password_data=="":
        messagebox.showerror(title="Opps",message="Please don't leave any fields empty!")

    else:
        try:
          with open("data.json","r")as file:
            data=json.loads(file.read())

        except FileNotFoundError:
            with open("data.json","w") as file:
               json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w")as file:
                json.dump(data,file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

def search_data():
    website=website_entry.get().title()
    try:
        with open("data.json","r") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showerror(
            title="Error",
            message="No data File Found"
        )
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]

            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showerror(
                title="Error",
                message=f"No detail for {website} exists"
            )


"""-------------------UI SetUP--------------"""
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
canvas.grid(row=0,column=1,columnspan=2,pady=(0,20))

website_label=Label(text="Website")
website_label.grid(row=1,column=0,sticky='e', padx=8, pady=8,)
email_Label=Label(text="Email/Username:")
email_Label.grid(row=2,column=0,sticky='e', padx=8, pady=8,)
password_label=Label(text="Password")
password_label.grid(row=3,column=0,sticky='e', padx=8, pady=8,)


# Entries
website_frame=Frame(window)
website_frame.grid(row=1, column=1, columnspan=2, pady=5)

website_entry = Entry(website_frame,width=30)
website_entry.pack(side="left")

search_button = Button(website_frame,text="Search",width=14,command=search_data)
search_button.pack(side="left", padx=2)

email_entry=Entry(width=45)
email_entry.grid(row=2,column=1,columnspan=2,sticky='w', padx=8, pady=8,)
email_entry.insert(0,"Shubhamkoti89@gmail.com")  #"""he normal show krta starting la email ch """
password_frame = Frame(window)
password_frame.grid(row=3, column=1, columnspan=2)

password_entry = Entry(password_frame, width=30)
password_entry.pack(side="left")

generate_password_button = Button(password_frame,text="Generate Password",
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
