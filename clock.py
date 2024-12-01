from tkinter import *

width = int(input("Введіть ширину (рекомендовано 270): "))
height = int(input("Введіть висоту (рекомендовано 270): "))
color1 = input("Введіть перший колір (рекомендовано red): ")
color2 = input("Введіть другий колір (рекомендовано blue): ")
color3 = input("Введіть третій колір (рекомендовано yellow): ")
color4 = input("Введіть третій колір (рекомендовано green): ")

root = Tk()
root.title("Figures")
root.geometry(f"{width}x{height}")

canva = Canvas(root, width=width, height=height)
canva.place(x=0, y=0)
canva.create_arc(0.037*width, 0.037*height, 0.963*width, 0.963*height, start=90, extent=90, fill=color2, width=3)
canva.create_arc(0.037*width, 0.037*height, 0.963*width, 0.963*height, start=0, extent=90, fill=color3, width=3)
canva.create_arc(0.037*width, 0.037*height, 0.963*width, 0.963*height, start=-90, extent=90, fill=color1, width=3)
canva.create_arc(0.037*width, 0.037*height, 0.963*width, 0.963*height, start=180, extent=90, fill=color4, width=3)
canva.create_line(0.5*width, 0.5*height, 0.1724*width, 0.1724*height, width=3)
canva.create_line(0.5*width, 0.5*height, 0.1724*width, 0.828*height, width=3)
canva.create_line(0.5*width, 0.5*height, 0.828*width, 0.1724*height, width=3)
canva.create_line(0.5*width, 0.5*height, 0.828*width, 0.828*height, width=3)
canva.create_oval(0.269*width, 0.269*height, 0.704*width, 0.704*height, fill="white", width=3)
canva.create_oval(0.481*width, 0.481*height, 0.519*width, 0.519*height, fill="black", width=3)
canva.create_line(0.5*width, 0.5*height, 0.5*width, 0.407*height, width=4)
canva.create_line(0.5*width, 0.5*height, 0.556*width, 0.481*height, width=4)

# 10 - 0.037x
# 135 - 0.5x
# 260 - 0.963x
# 46.555 - 0.1724x
# 223.555 - 0.828x
# 80 - 0.269x
# 190 - 0.704x
# 130 - 0.481x
# 140 - 0.519x
# 110 - 0.407x
# 150 - 0.556x

root.mainloop()
