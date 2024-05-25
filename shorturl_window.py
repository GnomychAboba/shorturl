from tkinter import *
from tkinter import messagebox
from config import *
from urllib.parse import urlparse
from pyshorteners import Shortener
from pyshorteners.exceptions import ShorteningErrorException
from pyperclip import copy

# проверка, является-ли ссылкой
def url_is_valid(url):
    result = urlparse(url)
    return all([result.scheme, result.netloc])

# копирование      
def copy_res():
    url = link2.get()
    copy(url)
   
# сокращение ссылок
def short_url():
    try:
        if url_is_valid(link1.get()):
            url = link1.get()
            shorts = Shortener().tinyurl.short(url)
            link2.delete(0,END)
            link2.insert(0, shorts)
        else:
            messagebox.showerror(Name, ERROR_IS_NOT_VALID)
    except ShorteningErrorException:
        messagebox.showerror(Name, ERROR_IS_SHORTED)

if __name__ == '__main__':
    # create window 
    window = Tk()
    window.title(Name)
    window.geometry(Resolution)
    window.resizable(width=False, height=False)
    window['bg'] = Background_color
    # add elements 
    label1 = Label(window, text=label1_text, font=Font,bg=Background_color,fg=Font_Background).pack(padx=5, pady=10)
    link1 = Entry(window, width=40)
    link1.pack(padx=5, pady=5)
    label2 = Label(window, text=label2_text, font=Font,bg=Background_color,fg=Font_Background).pack(padx=5, pady=10)
    link2 = Entry(window, width=40)
    link2.pack(padx=5, pady=5)
    button1 = Button(window, text=button1_text, font=Font,command=short_url,bg=Background_color,fg=Font_Background).pack(padx=10, pady=10)
    button2 = Button(window, text=button2_text, font=Font,command=copy_res,bg=Background_color,fg=Font_Background).pack(padx=10, pady=10)
    # window init
    window.mainloop()
