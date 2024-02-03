import tkinter
canvas = tkinter.Canvas(width=500)
canvas.pack()

def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def stvorce(x, y, pocet, dlzka, r=255, g=255, b=255):
    for i in range(pocet):
        krok = 255 // pocet
        canvas.create_rectangle(x, y, x + dlzka, y + dlzka, fill=rgb(r, g, b))
        x += dlzka
        for i in range(pocet):
            krok = 255 // pocet
            canvas.create_rectangle(x - pocet, y + dlzka, x + dlzka - pocet, y + dlzka * 2, fill=rgb(r, g, b))

            for i in range(pocet):
                krok = 255 // pocet
                canvas.create_rectangle(x - pocet, y + dlzka * 2, x + dlzka - pocet, y + dlzka * 3,fill=rgb(r, g, b))
        if r > krok:
            r -= krok
        if g > krok:
            g -= krok
        if b > krok:
            b -= krok

stvorce(20, 20, 20, 20, 255, 0, 0)
stvorce(20, 20, 20, 20, 0, 255, 0)
stvorce(20, 20, 20, 20, 0, 0, 255)
tkinter.mainloop()