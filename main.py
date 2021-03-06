import tkinter as tk
from principalController import principalController
from principalView import *
from revisionView import *
from revisionController import *
from Modelo.tClient import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Revisiones Oculares')

        # create a view and place it on the root window
        # view = revisionView(self)
        view = principalView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = principalController(view)
        # controller = revisionController(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
