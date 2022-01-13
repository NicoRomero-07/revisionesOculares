import tkinter as tk

from principalController import principalController
from principalView import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Revisiones Oculares')

        # create a model
        #model = Model('hello@pythontutorial.net')

        # create a view and place it on the root window
        view = principalView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = principalController(view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()