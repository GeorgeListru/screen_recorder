import tkinter as tk

window = tk.Tk()
window.title('Video Recorder')
window.geometry('200x300')
window.resizable(False, False)
window.configure(background='#222222')

#create a text label
label = tk.Label(window, text='1920x1080, 60fps', font=('Arial', 12), fg='#ffffff', bg='#222222')
label.pack(side='top', pady=(30, 0))

record_icon = tk.PhotoImage(file='record_button.png').subsample(5, 5)
record_button= tk.Button(window, image=record_icon, bg='#222222', activebackground="#222222",bd=0, fg='#ffffff', relief='ridge', command=lambda: print('Record'))
record_button.pack(side='top', pady=(20, 0))

#create a settings button
settings_button= tk.Button(window, text='settings', font=('Arial', 12), fg='#ffffff', bg='#3C3C3C', activebackground="#3C3C3C", activeforeground="white",bd=0, relief='ridge', command=lambda: print('Settings'), width=15)
settings_button.pack(side='bottom', pady=(0, 20))

window.mainloop()