import tkinter

canvas = tkinter.Canvas(width=600, height=200)
canvas.pack()
x = 10
y = 10
d = 20

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
x = 6 * d
y = 10
d = 20
canvas.create_rectangle(x, y, x+d, y+d)
canvas.create_rectangle(x, y+d, x+d, y+2*d)
canvas.create_rectangle(x, y+2*d, x+d, y+3*d)
canvas.create_rectangle(x, y+3*d, x+d, y+4*d)
canvas.create_rectangle(x, y+4*d, x+d, y+5*d)
canvas.create_rectangle(x, y+5*d, x+d, y+6*d)
canvas.create_rectangle(x, y+6*d, x+d, y+7*d)

canvas.create_rectangle(x+d, y, x+2*d, y+d)
canvas.create_rectangle(x+2*d, y, x+3*d, y+d)
canvas.create_rectangle(x+3*d, y, x+4*d, y+d)
canvas.create_rectangle(x+4*d, y, x+5*d, y+d)

canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d)
canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d)

canvas.create_rectangle(x+d, y+6*d, x+2*d, y+7*d)
canvas.create_rectangle(x+2*d, y+6*d, x+3*d, y+7*d)
canvas.create_rectangle(x+3*d, y+6*d, x+4*d, y+7*d)
canvas.create_rectangle(x+4*d, y+6*d, x+5*d, y+7*d)
# pismeno T
x = 12 * d
y = 10
d = 20
canvas.create_rectangle(x, y, x+d, y+d)
canvas.create_rectangle(x+d, y, x+2*d, y+d)
canvas.create_rectangle(x+2*d, y, x+3*d, y+d)
canvas.create_rectangle(x+3*d, y, x+4*d, y+d)
canvas.create_rectangle(x+4*d, y, x+5*d, y+d)

canvas.create_rectangle(x+2*d, y+d, x+3*d, y+2*d)
canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d)
canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d)
canvas.create_rectangle(x+2*d, y+4*d, x+3*d, y+5*d)
canvas.create_rectangle(x+2*d, y+5*d, x+3*d, y+6*d)
canvas.create_rectangle(x+2*d, y+6*d, x+3*d, y+7*d)
# pismeno R
x = 18 * d
y = 10
d = 20
canvas.create_rectangle(x, y, x+d, y+d)
canvas.create_rectangle(x, y+d, x+d, y+2*d)
canvas.create_rectangle(x, y+2*d, x+d, y+3*d)
canvas.create_rectangle(x, y+3*d, x+d, y+4*d)
canvas.create_rectangle(x, y+4*d, x+d, y+5*d)
canvas.create_rectangle(x, y+5*d, x+d, y+6*d)
canvas.create_rectangle(x, y+6*d, x+d, y+7*d)

canvas.create_rectangle(x+d, y, x+2*d, y+d)
canvas.create_rectangle(x+2*d, y, x+3*d, y+d)
canvas.create_rectangle(x+3*d, y, x+4*d, y+d)

canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d)
canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d)

canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d)
canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d)

canvas.create_rectangle(x+2*d, y+4*d, x+3*d, y+5*d)
canvas.create_rectangle(x+3*d, y+5*d, x+4*d, y+6*d)
canvas.create_rectangle(x+4*d, y+6*d, x+5*d, y+7*d)
# pismeno A
x = 24 * d
y = 10
d = 20
canvas.create_rectangle(x+d, y, x+2*d, y+d)
canvas.create_rectangle(x+2*d, y, x+3*d, y+d)
canvas.create_rectangle(x+3*d, y, x+4*d, y+d)

canvas.create_rectangle(x, y+d, x+d, y+2*d)
canvas.create_rectangle(x, y+2*d, x+d, y+3*d)
canvas.create_rectangle(x, y+3*d, x+d, y+4*d,)
canvas.create_rectangle(x, y+4*d, x+d, y+5*d)
canvas.create_rectangle(x, y+5*d, x+d, y+6*d)
canvas.create_rectangle(x, y+6*d, x+d, y+7*d)

canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d)
canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d)
canvas.create_rectangle(x+4*d, y+3*d, x+5*d, y+4*d)
canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d)
canvas.create_rectangle(x+4*d, y+5*d, x+5*d, y+6*d)
canvas.create_rectangle(x+4*d, y+6*d, x+5*d, y+7*d)

canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d)
canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d)

canvas.mainloop()