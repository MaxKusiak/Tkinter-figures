from tkinter import *

width = int(input("Введіть ширину (рекомендовано 500): "))
height = int(input("Введіть висоту (рекомендовано 510): "))
color1 = input("Введіть перший колір (рекомендовано red): ")
color2 = input("Введіть другий колір (рекомендовано blue): ")
color3 = input("Введіть третій колір (рекомендовано yellow): ")

root = Tk()
root.title("Figures")
root.geometry(f"{width}x{height}")

canva = Canvas(root, width=width, height=height)
canva.place(x=0, y=30)
canva.create_line(0.1*width, 0.902*height, 0.9*width, 0.902*height, width=6) 
canva.create_polygon(0.42*width, 0.902*height, 0.46*width, 0.784*height, 0.54*width, 0.784*height, 0.58*width, 0.902*height, fill='black', outline='black')
canva.create_polygon(0.1*width, 0.784*height, 0.22*width, 0.608*height, 0.5*width, 0.608*height, 0.5*width, 0.784*height, fill=color1, outline='black', width=6)
canva.create_polygon(0.14*width, 0.608*height, 0.26*width, 0.431*height, 0.5*width, 0.608*height, fill=color1, outline='black', width=6)
canva.create_polygon(0.26*width, 0.431*height, 0.5*width, 0.431*height, 0.5*width, 0.608*height, fill=color2, outline='black', width=6)
canva.create_polygon(0.18*width, 0.431*height, 0.5*width, 0, 0.5*width, 0.431*height, fill=color2, outline='black', width=6)
canva.create_polygon(0.9*width, 0.784*height, 0.78*width, 0.608*height, 0.5*width, 0.608*height, 0.5*width, 0.784*height, fill=color3, outline='black', width=6)
canva.create_polygon(0.86*width, 0.608*height, 0.74*width, 0.431*height, 0.5*width, 0.608*height, fill=color3, outline='black', width=6)
canva.create_polygon(0.74*width, 0.431*height, 0.5*width, 0.431*height, 0.5*width, 0.608*height, fill=color1, outline='black', width=6)
canva.create_polygon(0.82*width, 0.431*height, 0.5*width, 0, 0.5*width, 0.431*height, fill=color1, outline='black', width=6)

# 220 - 0.431y
# 310 - 0.608y
# 400 - 0.784y
# 460 - 0.902y

# 50 - 0.1x
# 70 - 0.14x
# 90 - 0.18x
# 110 - 0.22x
# 130 - 0.26x
# 210 - 0.42x
# 230 - 0.46x
# 250 - 0.5x
# 270 - 0.54x
# 290 - 0.58x
# 370 - 0.74x
# 390 - 0.78x
# 410 - 0.82x
# 430 - 0.86x
# 450 - 0.9x

root.mainloop()
