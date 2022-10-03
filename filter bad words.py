from tkinter import *
from tkinter import ttk
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfile
import tkinter as tk
from better_profanity import profanity #bad word sensor library



class censor:
    def __init__(self,root):
        self.my_w =root
        self.my_w.title("Filter Bad Words")
        self.my_w .geometry('1350x300')


        l1 = tk.Label(self.my_w, text='Enter Custom Bad Words', width=30, font='Arial')
        l1.grid(row=1, column=1)
        l2 = tk.Label(self.my_w, text='Filter Bad Words', width=30, font='Arial')
        l2.place(x=650,y=0)
        l3 = tk.Label(self.my_w, text='Develop by : Tariq Ahmed :: Email: tariqktk2015@gmail.com', width=140, font='Arial')
        l3.place(x=0, y=240)

        self.t1 = tk.Text(self.my_w, width=40, height=10)
        self.t1.grid(row=2, column=1)


        self.t2 = tk.Text(self.my_w, width=40, height=10)
        self.t2.place(x=600,y=30)

        self.b1 = tk.Button(self.my_w, text='Save', command=lambda: self.save_file(), width=20)
        self.b1.place(x=100,y=200)

        b2 = tk.Button(self.my_w, text='IMPORT BAD WORDS FILE', command=lambda: self.select_file(), width=20)
        b2.place(x=380,y=100)


        b3 = tk.Button(self.my_w, text='IMPORT CENSOR FILE', command=lambda: self.select_file_checking(), width=20)
        b3.place(x=380,y=150)

        self.b4 = tk.Button(self.my_w, text='SAVE', command=lambda: self.censorfilesave(), width=20)
        self.b4.place(x=700,y=200)



    def save_file(self):
        my_str1 = self.t1.get("1.0", END)  # read from one text box t1
        fob = filedialog.asksaveasfile(filetypes=[('text file', '*.txt')],
                                       defaultextension='.txt', initialdir=os.getcwd(),
                                       mode='w')
        try:
            fob.write(my_str1)
            fob.close()
            self.t1.delete('1.0', END)  # Delete from position 0 till end
            self.t1.update()
            self.b1.config(text="Saved")
            self.b1.after(3000, lambda: self.b1.config(text='Save'))
            messagebox.showinfo("saved", 'Saved')
        except:
         messagebox.showerror("Error", "Please save")



    def select_file(self):

        self.filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        self.filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir=os.getcwd(),
            filetypes=self.filetypes)

        showinfo(
            title='Selected File',
            message=self.filename

        )
        #print(self.filename) #print file path of bad words
        self.file = open(self.filename, 'r')
        self.content = self.file.read()
        # print(self.content)  #print text from of bad words

        '''
        use this keywords to aaccess path and text
        path:
        self.filename
        text accces:
        self.content
        '''

        #---------------------------------------------------------------
    def select_file_checking(self):
        self.filetypes_c = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        self.filename_c = filedialog.askopenfilename(
            title='Open a file',
            initialdir=os.getcwd(),
            filetypes=self.filetypes_c)

        showinfo(
            title='Selected File',
            message=self.filename_c

        )


        '''
        use this keywords to aaccess path and text
        path:
        self.filename_c
        text accces:
        self.content_c
        '''

        #print(self.filename_c)  #print path of checking file

        self.file_c = open(self.filename_c, 'r')
        self.content_c = self.file_c.read()
        #print(self.content_c) #print text from checking file

        # load bad words from file
        open_file = profanity.load_censor_words_from_file(self.filename)
        # print content
        #print(profanity.censor(self.content_c))
        self.censorwords=profanity.censor(self.content_c)
        print(self.censorwords)


        #-----------------------------------------
        # after censor read these and save into text file
        self.t2.insert('1.0', self.censorwords)

    def censorfilesave(self):
        my_str1 = self.t2.get("1.0", END)  # read from one text box t1
        fob = filedialog.asksaveasfile(filetypes=[('text file', '*.txt')],
                                       defaultextension='.txt', initialdir=os.getcwd(),
                                       mode='w')

        try:
            fob.write(my_str1)
            fob.close()
            self.t2.delete('1.0', END)  # Delete from position 0 till end
            self.t2.update()
            self.b4.config(text="Saved")
            self.b4.after(3000, lambda: self.b4.config(text='Save'))

            messagebox.showinfo("saved", 'Saved')
        except:
            messagebox.showerror("Error", "Please save")







if __name__=="__main__":
    root=Tk()
    obj=censor(root)
    root.mainloop()

