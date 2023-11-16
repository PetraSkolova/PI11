import tkinter
import random

canvas = tkinter.Canvas(width = 600, height = 500)
canvas.pack()
"""""
x = 3
xx = x
y = 10
d = 30

pocet = 598 // d    # // je celociselne delenie 7 // 3 = 2
for j in range(498 // d):
    for i in range(pocet):
        color = random.choice(("green", "red", "blue", "orange", "purple"))
        canvas.create_rectangle(x, y, x+d, y+d, fill = color)
        canvas.create_line(x, y, x+d, y+d)
        canvas.create_line(x, y+d, x+d, y)
        x = x + d  #nakresli stvorcek vedla dalsieho stvorceka
    y = y + d
    x = xx
"""


x = 50
xx = x
y = 50
d = 80
stvrtina = d // 4

#canvas.create_rectangle(x,  y+d // 2, x+d, y+(d // 2)+d)
#canvas.create_polygon(x + d // 2, y, x+d, x+d, y+(d // 2)+d, x + d // 2, y)
canvas.create_rectangle(x,  y+d // 2, x+d, y+(d // 2)+d, fill="orange")
canvas.create_polygon(x, y+d//2, x+2*stvrtina, y, x+d, y+d//2, outline="black", fill="red")
canvas.create_rectangle(x+stvrtina, y+d // 2+stvrtina, x+3*stvrtina, y+d // 2+3*stvrtina, fill="light blue")
#canvas.create_line(x+stvrtina, y+d // 2+2*stvrtina, x+3*stvrtina,y+d // 2+2*stvrtina)
#canvas.create_line()
canvas.create_line(x+stvrtina, y+d // 2+2*stvrtina, x+3*stvrtina,y+d // 2+2*stvrtina)
canvas.create_line(x+2*stvrtina, y+d // 2+stvrtina, x+2*stvrtina, y+d // 2+3*stvrtina)


canvas.mainloop()
