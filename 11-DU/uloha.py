import tkinter

canvas = tkinter.Canvas()
canvas.pack()
x = 10
y = 10
d = 20
color = "magenta"

# pismeno P
canvas.create_rectangle(x, y, x+d, y+d)
canvas.create_rectangle(x, y+d, x+d, y+2*d)
canvas.create_rectangle(x, y+2*d, x+d, y+3*d)
canvas.create_rectangle(x, y+3*d, x+d, y+4*d)
canvas.create_rectangle(x, y+4*d, x+d, y+5*d)
canvas.create_rectangle(x, y+5*d, x+d, y+6*d)
canvas.create_rectangle(x, y+6*d, x+d, x+7*d)

canvas.create_rectangle(x+d, y, x+2*d, y+d)
canvas.create_rectangle(x+2*d, y, x+3*d, y+d)
canvas.create_rectangle(x+3*d, y, x+4*d, y+d)

canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d)
canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d)

canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d)
canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d)
# pismeno E
x = 10
y = 10
d = 20
canvas.create_rectangle(x+6*d, y, x+7*d, y+d)
canvas.create_rectangle(x+6*d, y+d, x+7*d, y+2*d)
canvas.create_rectangle(x+6*d, y+2*d, x+7*d, y+3*d)
canvas.create_rectangle(x+6*d, y+3*d, x+7*d, y+4*d)
canvas.create_rectangle(x+6*d, y+4*d, x+7*d, y+5*d)
canvas.create_rectangle(x+6*d, y+5*d, x+7*d, y+6*d)
canvas.create_rectangle(x+6*d, y+6*d, x+7*d, y+7*d)

canvas.create_rectangle(x+7*d, y, x+8*d, y+d)
canvas.create_rectangle(x+8*d, y, x+9*d, y+d)
canvas.create_rectangle(x+9*d, y, x+10*d, y+d)
canvas.create_rectangle(x+10*d, y, x+11*d, y+d)

canvas.create_rectangle(x+7*d, y+3*d, x+8*d, y+4*d)
canvas.create_rectangle(x+8*d, y+3*d, x+9*d, y+4*d)
canvas.create_rectangle(x+9*d, y+3*d, x+10*d, y+4*d)

canvas.create_rectangle(x+7*d, y+6*d, x+8*d, y+7*d)
canvas.create_rectangle(x+8*d, y+6*d, x+9*d, y+7*d)
canvas.create_rectangle(x+9*d, y+6*d, x+10*d, y+7*d)
canvas.create_rectangle(x+10*d, y+6*d, x+11*d, y+7*d)


canvas.mainloop()