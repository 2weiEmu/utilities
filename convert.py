# Import required libraries
from tkinter import Tk, Text, Button, END
import re

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create a text widget
my_clip = Text(win, height=15)
my_clip.pack()


def update_text():
    global my_clip
    # my_clip.insert(END,pyperclip.paste())
    text = (my_clip.get("1.0", "end-1c"))

    lines = text.split("\n")

    # c_times = len(lines[0].split(" "))
    c_times = max([len(re.findall('"([^"]*)"', x)) for x in lines])

    out_text = "\\begin{tabular}" + "{" + (c_times * "|c") + "|}\n"

    for line in lines:
        single = "\t"
        key = re.findall('"([^"]*)"', line)
        for k in key:
            single += k+" & "
        single = single[:-3] + "\\\\ \n"
        out_text += single

    out_text += "\\end{tabular}"

    my_clip.insert(END, "\n"+out_text)


# Create a button to paste the copied text from clipboard
button = Button(win, text="Paste Here", command=update_text)
button.pack()

win.mainloop()

"""
"title_id" "genre"
"something" "number"
"more" "number"
"""
