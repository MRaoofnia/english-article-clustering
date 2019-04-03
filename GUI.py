from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from main import cluster


def isfloat(x):
    for char in x:
        if char not in ['1','2','3','4','5','6','7','8','9','0','.']:
            return False
    return True

def main():
    root = Tk()
    root.title("English Articles Clustering Tool")
    mainframe = ttk.Frame(root, padding = "12 12 12 12")
    mainframe.grid(column = 0, row = 0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)

    URL = StringVar(value = "not available!")
    threshold = StringVar()
    savepath = StringVar()
    savepath.set(os.getcwd())

    URLentry = ttk.Entry(mainframe, width = 30, textvariable = URL, stat = DISABLED)
    URLentry.grid(column = 2, row = 1, sticky = (W,E))
    thresholdentry = ttk.Entry(mainframe, width = 10, textvariable = threshold)
    thresholdentry.grid(column = 2, row = 2, sticky = W)
    savepathentry = ttk.Entry(mainframe, width = 30, textvariable = savepath)
    savepathentry.grid(column = 2, row = 3, sticky = (W,E))
    
    ttk.Label(mainframe, text = "URL:").grid(column = 1, row = 1, sticky = E)
    ttk.Label(mainframe, text = "threshold value:").grid(column = 1, row = 2, sticky = E)
    ttk.Label(mainframe, text = "save to:").grid(column = 1, row = 3, sticky = E)

    def choosedir():
        savepath.set(filedialog.askdirectory(parent=root, initialdir= "./", title='Please select a directory'))
    def start():
        #getting and checking values
        url = URL.get()
        thresholdstring = threshold.get()
        if thresholdstring == "":
            thresholdstring = "0"
        path = savepath.get()
        if not os.path.isdir(path):
            messagebox.showerror("Error", "Enter a valid path, please.")
        elif not isfloat(thresholdstring):
            messagebox.showerror("Error", "Threshold value should be a number, please enter a valid one.")
        else:
            messagebox.showinfo("Clustering","It's getting data and clustering now. don't panic if it seems stuck. it may take 5 minutes...")
            cluster(path, float(thresholdstring))
            messagebox.showinfo(title = "succesful", message = "Succesfully saved to %s/output.json"%path)    
            

    ttk.Button(mainframe, text = "open", command = choosedir).grid(column = 3, row = 3, sticky = (W,E))
    ttk.Button(mainframe, text = "Start", command = start).grid(column = 3, row = 4, sticky = (W,E))
    ttk.Button(mainframe, text = "Cancel", command = root.destroy).grid(column = 2, row = 4, sticky = (W,E))
    
    

    root.mainloop()


if __name__ == "__main__":
    main()