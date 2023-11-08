import tkinter

canvas = tkinter.Canvas()
canvas.pack()
x = 10
y = 10
d = 20
color = "purple"

canvas.create_rectangle(x, y, x+d, y+d, fill = color)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill = color)
canvas.create_rectangle( x+2*d, y+2*d, x+3*d, x+3*d, fill = color)
canvas.create_rectangle( x+3*d, y+3*d, x+4*d, x+4*d, fill = color)
canvas.create_rectangle( x+4*d, y+4*d, x+5*d, x+5*d, fill = color)
canvas.create_rectangle(x, y+4*d, x+d, x+5*d, fill = color)
canvas.create_rectangle( x+d, y+3*d, x+2*d, y+4*d, fill = color)
canvas.create_rectangle( x+3*d, y+d, x+4*d, y+2*d, fill = color)
canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill = color)

canvas.mainloop()

x = 6 * d
y = 10
d = 20
color = "purple"

canvas.create_rectangle(x, y, x+d, y+d, fill = color)
canvas.create_rectangle(x+d, y+d, x+2d, y+2d, fill = color)
canvas.create_rectangle( x+2d, y+2d, x+3d, x+3d, fill = color)
canvas.create_rectangle( x+3d, y+3d, x+4d, x+4d, fill = color)
canvas.create_rectangle( x+4d, y+4d, x+5d, x+5d, fill = color)
canvas.create_rectangle(x, y+4d, x+d, x+5d, fill = color)
canvas.create_rectangle( x+d, y+3d, x+2d, y+4d, fill = color)
canvas.create_rectangle( x+3d, y+d, x+4d, y+2d, fill = color)
canvas.create_rectangle(x+4d, y, x+5d, y+d, fill = color)