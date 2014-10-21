##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#Making a rectangle that goes slightly off of the page onto and filled with green
grass = drawpad.create_rectangle(0,550,805,605, fill = "green")

#Making the body of the house
housebody = drawpad.create_rectangle(250,300,550,550, fill = "red")

#Making the roof of the house
leftroof = drawpad.create_line(250,300,400,200)
rightroof = drawpad.create_line(400,200,550,300)

#Making the door of the house
door = drawpad.create_rectangle(350,400,450,550, fill = "lightblue")

#making windows for the house
#windows = 

root.mainloop()