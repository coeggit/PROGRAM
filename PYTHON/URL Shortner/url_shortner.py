from tkinter import *
import pyshorteners
import clipboard

root = Tk()
root.title("Url")
root.geometry("470x120")
root.resizable(False, False)

# Short Url Fuction
def shorten():
    try : 
        url = url_entry.get()
        final_result = pyshorteners.Shortener().tinyurl.short(url)
        str_url.set(final_result)
        url_entry.delete(0, END)
        
        print(final_result)
    except : 
        str_url.set("Enter Url Please")

# Copy Short Url Function
def copy_text():
    try : 
        clipboard.copy(str_url.get())
        print("Url Copied Successfully!!")
    except : 
        str_url.set("Something Wrong Try Again!!")


# Input Url
url_label = Label(root, text="Masukkan Link URL")
url_label.grid(row=1, column=0, padx=5, pady=5)

url_entry = Entry(root, width=40, justify=CENTER)
url_entry.grid(row=1, column=1, padx=5, pady=5)

# Shorten Link Button
shorten_but = Button(root, text="Shorten Link", command=shorten, width=20)
shorten_but.grid(row=3, column=1, padx=4, pady=4)

# Shorterned Link
shorty_label = Label(root, text="Shortened Link")
shorty_label.grid(row=2, column=0, padx=5, pady=5)

str_url = StringVar(root)
shorty_entry = Entry(root, width=35, textvariable=str_url, justify=CENTER)
shorty_entry.grid(row=2, column=1, padx=5, pady=5)

# Copy Button
copy_but = Button(root, text="Copy", command=copy_text, width=10)
copy_but.grid(row=2, column=2, padx=1, pady=1)


root.mainloop()