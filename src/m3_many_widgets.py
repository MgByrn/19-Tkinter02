import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
frame1 = tk.Frame(window, bg = "cadetblue")
frame1.pack(side=tk.LEFT)  

label1 = tk.Label(frame1, text="Book Title", bg = "ghost white")
label1.pack()

button1 = tk.Button(frame1, text="Name", bg="ghost white")
button1.pack()

entry1 = tk.Entry(frame1)
entry1.pack()

frame2 = tk.Frame(window, bg="cadetblue")
frame2.pack(side=tk.RIGHT)   

label2 = tk.Label(frame2, text="Text",bg="ghost white")
label2.pack()

text2 = tk.Text(frame2, height=5, width=30)  
text2.pack()

window.mainloop()