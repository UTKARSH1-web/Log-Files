
from tkinter import BOTH, NO, Button, OptionMenu, StringVar, Tk, ttk
import pandas as pd

file_name = "logfile.log"
file = open(file_name, "r")
data = []
order = ["date", "type", "message"]
pd.set_option("display.max_colwidth", -1)
df = pd.DataFrame(columns=["date", "type", "messages"])
df1 = pd.DataFrame(columns=["date", "type", "messages"])
df2 = pd.DataFrame(columns=["date", "type", "messages"])
df3 = pd.DataFrame(columns=["date", "type", "messages"])
df4 = pd.DataFrame(columns=["date", "type", "messages"])

for line in file.readlines():
    details = line.split("|")
    details = [x.strip() for x in details]
    structure = {key: value for key, value in zip(order, details)}
    if structure["type"] == "ERROR":
        df = df.append({"date": structure["date"], "type": "ERROR", "messages": structure["message"]},
                       ignore_index=True)
    if structure["type"] == "INFO":
        df1 = df1.append({"date": structure["date"], "type": "INFO", "messages": structure["message"]},
                         ignore_index=True)
    if structure["type"] == "DEBUG":
        df2 = df2.append({"date": structure["date"], "type": "DEBUG", "messages": structure["message"]},
                         ignore_index=True)
    if structure["type"] == "WARNING":
        df3 = df3.append({"date": structure["date"], "type": "WARNING", "messages": structure["message"]},
                         ignore_index=True)
    if structure["type"] == "CRITICAL":
        df4 = df4.append({"date": structure["date"], "type": "CRITICAL", "messages": structure["message"]},
                         ignore_index=True)
df.reset_index(drop=True, inplace=True)
df1.reset_index(drop=True, inplace=True)
df2.reset_index(drop=True, inplace=True)
df3.reset_index(drop=True, inplace=True)
df4.reset_index(drop=True, inplace=True)
root = Tk()
root.geometry("600x600")


def selected():
    if menu.get() == "ERROR":

        cols = list(df.columns)

        tree = ttk.Treeview(root)

        tree.column("#0", stretch=NO, width=50)
        tree.pack(fill=BOTH, expand=0)

        def clear():
            tree.destroy()
            myButton2.destroy()

        myButton2 = Button(root, text="clear", command=clear)
        myButton2.pack()
        tree["columns"] = cols
        tree.column("#0", stretch=NO, width=50)
        for i in cols:
            if i == "date":
                tree.column(i, anchor="w", stretch=NO, width=250)
                tree.heading(i, text=i, anchor='w')
            elif i == "type":
                tree.column(i, anchor="w", stretch=NO, width=150)
                tree.heading(i, text=i, anchor='w')
            else:
                tree.column(i, anchor="w")
                tree.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tree.insert("", 16, text=index, values=list(row))

    if menu.get() == "INFO":

        cols = list(df1.columns)
        tree = ttk.Treeview(root)

        def clear():
            tree.destroy()
            myButton2.destroy()

        myButton2 = Button(root, text="clear", command=clear)
        myButton2.pack()

        tree.pack(fill=BOTH, expand=0)
        tree["columns"] = cols
        tree.column("#0", stretch=NO, width=50)
        for i in cols:
            for i in cols:
                if i == "date":
                    tree.column(i, anchor="w", stretch=NO, width=250)
                    tree.heading(i, text=i, anchor='w')
                elif i == "type":
                    tree.column(i, anchor="w", stretch=NO, width=150)
                    tree.heading(i, text=i, anchor='w')
                else:
                    tree.column(i, anchor="w")
                    tree.heading(i, text=i, anchor='w')
        for index, row in df1.iterrows():
            tree.insert("", 16, text=index, values=list(row))
    if menu.get() == "DEBUG":

        cols = list(df.columns)

        tree = ttk.Treeview(root)

        tree.column("#0", stretch=NO, width=50)
        tree.pack(fill=BOTH, expand=0)

        def clear():
            tree.destroy()
            myButton2.destroy()

        myButton2 = Button(root, text="clear", command=clear)
        myButton2.pack()
        tree["columns"] = cols
        tree.column("#0", stretch=NO, width=50)
        for i in cols:
            if i == "date":
                tree.column(i, anchor="w", stretch=NO, width=250)
                tree.heading(i, text=i, anchor='w')
            elif i == "type":
                tree.column(i, anchor="w", stretch=NO, width=150)
                tree.heading(i, text=i, anchor='w')
            else:
                tree.column(i, anchor="w")
                tree.heading(i, text=i, anchor='w')

        for index, row in df2.iterrows():
            tree.insert("", 16, text=index, values=list(row))

    if menu.get() == "WARNING":

        cols = list(df1.columns)
        tree = ttk.Treeview(root)

        def clear():
            tree.destroy()
            myButton2.destroy()

        myButton2 = Button(root, text="clear", command=clear)
        myButton2.pack()

        tree.pack(fill=BOTH, expand=0)
        tree["columns"] = cols
        tree.column("#0", stretch=NO, width=50)
        for i in cols:
            for i in cols:
                if i == "date":
                    tree.column(i, anchor="w", stretch=NO, width=250)
                    tree.heading(i, text=i, anchor='w')
                elif i == "type":
                    tree.column(i, anchor="w", stretch=NO, width=150)
                    tree.heading(i, text=i, anchor='w')
                else:
                    tree.column(i, anchor="w")
                    tree.heading(i, text=i, anchor='w')
        for index, row in df3.iterrows():
            tree.insert("", 16, text=index, values=list(row))
    if menu.get() == "CRITICAL":

        cols = list(df.columns)

        tree = ttk.Treeview(root)

        tree.column("#0", stretch=NO, width=50)
        tree.pack(fill=BOTH, expand=0)

        def clear():
            tree.destroy()
            myButton2.destroy()

        myButton2 = Button(root, text="clear", command=clear)
        myButton2.pack()
        tree["columns"] = cols
        tree.column("#0", stretch=NO, width=50)
        for i in cols:
            if i == "date":
                tree.column(i, anchor="w", stretch=NO, width=250)
                tree.heading(i, text=i, anchor='w')
            elif i == "type":
                tree.column(i, anchor="w", stretch=NO, width=150)
                tree.heading(i, text=i, anchor='w')
            else:
                tree.column(i, anchor="w")
                tree.heading(i, text=i, anchor='w')

        for index, row in df4.iterrows():
            tree.insert("", 16, text=index, values=list(row))


menu = StringVar()
menu.set("Select type")
drop = OptionMenu(root, menu, "ERROR", "DEBUG", "WARNING", "CRITICAL", "INFO")
print(menu)
drop.pack()
myButton = Button(root, text="select", command=selected)
myButton.pack()
root.mainloop()