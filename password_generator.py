from tkinter import *
import string
import secrets
import sqlite3
from datetime import datetime


root = Tk()
root.title('Password generator')
root.geometry('350x450')
root.iconbitmap('Pictures/p_app.ico')

input_frame = Frame(root, padx=10, pady=10)
input_frame.pack()
output_frame = Frame(root, padx=10, pady=10)
output_frame.pack()


def save():
    # SQL stuff
    conn = sqlite3.connect('passwords.db')
    cur = conn.cursor()
    # cur.execute('''
    # CREATE TABLE passwords (
    #     Login VARCHAR(50) NOT NULL,
    #     Link VARCHAR(300),
    #     Password VARCHAR(30) NOT NULL,
    #     last_update TIMESTAMP NOT NULL,
    # UNIQUE (description)
    # );
    # ''')
    cur.execute('''INSERT INTO passwords (description, link, password, last_update) VALUES ('{}', '{}', '{}', '{}');
    '''.format(description.get(), website.get(), password, datetime.now().strftime("%d:%m:%Y")))
    conn.commit()
    cur.close()
    conn.close()
    description.delete(0, END)
    website.delete(0, END)


def func():
    global password
    for widget in output_frame.winfo_children():
        widget.grid_forget()
    ready = False
    password = None
    result = Label(input_frame)
    while not ready:
        length = int(pass_len.get())
        alphabet = ''
        result.destroy()
        # Create alphabet and password
        for n, option in enumerate(options):
            if options[option_labels[n]][0].get():
                alphabet = alphabet + options[option_labels[n]][1]
        try:
            password = ''.join(secrets.choice(alphabet) for _ in range(length))
        except IndexError:
            result = Label(output_frame, text="Pick at least one option").grid(row=0, column=0, sticky='w',
                                                                               pady=10, ipadx=5)

        ready = True
        # Check if all conditions are provided
        for n, option in enumerate(options):
            if not check(options[option_labels[n]][0].get(), options[option_labels[n]][1], password):
                ready = False
    if password:
        Label(output_frame, text="Your password is: {}".format(password)).grid(row=0, column=0, sticky='w', pady=10,
                                                                               ipadx=5, columnspan=2)
        Label(output_frame, text='Login').grid(row=1, column=0)
        Label(output_frame, text='Link').grid(row=1, column=1)

        # website = Entry(output_frame)
        description.grid(row=2, column=0)
        website.grid(row=2, column=1)
        Button(output_frame, text='Save', width=15, command=save).grid(row=3, column=0, columnspan=2, pady=15)


def check(condition, content, result):
    if condition:
        for k in content:
            if k in result:
                return True
    else:
        return True
    return False


labels = ['Password length', 'Include symbols', 'Include numbers', 'Include lowercase chars', 'Include uppercase chars']
option_labels = ['(e.g. @#$%)', '(e.g. 123456789)', 'e.g. abcdef..', 'e.g. ABCDEF..']
option_content = ['!@#$%^&*|~', string.digits, string.ascii_lowercase, string.ascii_uppercase, '']

options = {}

for i, label in enumerate(labels):
    Label(input_frame, text=label).grid(row=i, column=0, sticky='w', pady=10, ipadx=5)


pass_len = StringVar()
pass_len.set('10')
OptionMenu(input_frame, pass_len, '10', '15', '20', '30').grid(row=0, column=1)

for i, label in enumerate(option_labels):
    options[label] = [BooleanVar(), option_content[i]]
    c = Checkbutton(input_frame, text=label, variable=options[option_labels[i]][0]).grid(row=i+1, column=1, sticky='w')

Button(input_frame, text='Create password', command=func).grid(row=len(labels)+1, column=0, sticky='w', pady=20)
description = Entry(output_frame)
website = Entry(output_frame)

root.mainloop()
