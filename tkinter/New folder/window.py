import Tkinter as tk

root = tk.Tk()
root.title('counting seconds')
logo = tk.PhotoImage(file='c:/users/abastillasgl/desktop/20170916_141826.gif')
text = '''
This is an
    example
    preformatted
  text thing
  ----
----
'''

# Labels to test out text, images, text-image combination,and changes to
# text visuals
w1 = tk.Label(root, image=logo).pack(side='right')
w2 = tk.Label(root, justify=tk.CENTER, padx=10, text=text).pack(side='left')
w3 = tk.Label(root,
              image=logo, text=text, compound=tk.CENTER,
              fg='white', bg='black', font='Calibri 20 italic').pack()

# Dynamic label and buttom example
counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter), fg = '#FF9938' if not (counter % 2) else '#80bbc3')
        label.after(1000, count)
    count()

label = tk.Label(root, fg='green')
label.pack()
counter_label(label)
button = tk.Button(root, text='stop', width=25, command=root.destroy).pack()

root.mainloop()
