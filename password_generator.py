from tkinter import *
import string
import secrets

root = Tk()
root.title('Password generator')
root.geometry('350x400')

input_frame = Frame(root, padx=10, pady=10)
input_frame.pack()
output_frame = Frame(root, padx=10, pady=10)
output_frame.pack()


def func():
    for widget in output_frame.winfo_children():
        widget.destroy()
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
        Label(output_frame, text="Your password is: {}".format(password)).grid(row=10, column=0, sticky='w', pady=10, ipadx=5)


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

root.mainloop()
