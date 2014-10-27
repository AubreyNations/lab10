from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#Making the sky.
sky = drawpad.create_rectangle(0,0,800,600, fill = "lightblue")

#Making a rectangle that goes slightly off of the page onto and filled with green. This is the grass.
grass = drawpad.create_rectangle(0,550,805,605, fill = "green")

#Making the body of the house
housebody = drawpad.create_rectangle(250,300,550,550, fill = "red")

#Making the roof of the house
roof = drawpad.create_polygon(250,300,400,200,550,300, fill = "pink", outline = "black")

#Making the door of the house
door = drawpad.create_rectangle(350,400,450,550, fill = "pink")

#making windows for the house
windows = drawpad.create_rectangle(275,400,325,350, fill = "lightblue")
windows2 = drawpad.create_rectangle(475,400,525,350, fill = "lightblue")

#Making the door knob for the house
doorknob = drawpad.create_oval(425,500,435,490, fill = "yellow", outline = "red")

#Making the chimney for the house
chimney = drawpad.create_polygon(480,225,480,255,545,225,545,297, fill = "pink", outline = "black")
topchimney = drawpad.create_rectangle(475,200,550,225, fill = "red")

#An awesome sun! So inspiring. So beautiful. Yes.
sun = drawpad.create_oval(50,50,150,150, fill = "yellow")

root.mainloop()