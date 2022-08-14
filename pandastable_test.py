from tkinter import *
from pandastable import Table, TableModel, config
import pandas as pd

class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('Table app')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            # df = TableModel.getSampleData()
            self.table = pt = Table(f, dataframe=data,
                                    showtoolbar=True, showstatusbar=True)
            pt.show()
            #set some options
            options = {'colheadercolor':'green','floatprecision': 5}
            config.apply_options(options, pt)
            pt.show()
            return
data = pd.read_csv('logs.txt', sep="|", header=None)
data.columns = ["TimeStamp", "Level", "Payload"]
app = TestApp()
#launch the app
app.mainloop()