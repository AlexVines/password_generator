from tkinter import *
import string
import secrets

root = Tk()
root.title('Password generator')
root.geometry('350x400')

input_frame = Frame(root, padx=10, pady=10)
input_frame.pack()


def func():
    ready = False
    password = ''
    while not ready:
        length = int(pass_len.get())
        alphabet = ''

        # Create alphabet
        for n, option in enumerate(options):
            if options[option_labels[n]][0].get():
                alphabet = alphabet + options[option_labels[n]][1]
        password = ''.join(secrets.choice(alphabet) for _ in range(length))

        # Check if all conditions are provided
        conditions_count = 0
        for n, option in enumerate(options):
            if check(options[option_labels[n]][0].get(), options[option_labels[n]][1], password):
                ready = True

    print(password)


def check(condition, content, result):
    if condition:
        for k in content:
            if k in result:
                return True
    return False


labels = ['Password length', 'Include symbols', 'Include numbers', 'Include lowercase chars', 'Include uppercase chars',
          'Don\'t repeat symbols']
option_labels = ['(e.g. @#$%)', '(e.g. 123456789)', 'e.g. abcdef..', 'e.g. ABCDEF..',
                 'Do not include similar symbols']
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
