from tkinter import *
from a_star import main, get_path
from board_reader import get_node_list
from math import inf


class Display:

    def __init__(self, master):
        # Creating frame for button
        frame = Frame(master)
        frame.pack()

        # Creating button
        self.quit_button = Button(frame, text="QUIT", command=frame.quit)
        self.quit_button.pack(side=LEFT)

        self.color_dict = {
            inf: "black",
            100: "blue",
            50: "gray",
            10: "forest green",
            5: "lawn green",
            1: "brown",
        }

    def setup_canvas(self, master, width, height):
        self.canvas = Canvas(master, width=width, height=height)
        self.canvas.pack()

    def paint_gui(self):
        node_list = get_node_list()
        path = get_path()
        number_in_grid = 0
        for y in range(0, 70, 10):
            for x in range(0, 200, 10):
                fill_color = self.color_dict.get(node_list[number_in_grid])
                if (y // 10, x // 10) in path:
                    fill_color = "gold"
                number_in_grid += 1
                self.canvas.create_rectangle(x, y, x + 10, y + 10, fill=fill_color, outline="black")


# Declaring tkinter root
root = Tk()

main('boards/board-1-1.txt')

display = Display(root)
display.setup_canvas(root, 200, 70)
display.paint_gui()

root.mainloop()
