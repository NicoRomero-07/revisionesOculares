from db import *
from sqlalchemy import *
from revisionView import revisionView
from revisionController import revisionController
from Modelo.tClient import tClient


class principalController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.url = 'mysql://root:1234@localhost:3306/mydb'

    def revisiones(self, nif, app):
        try:
            if nif != "":
                app.title('Revisiones Oculares')

                view = revisionView(app)
                view.grid(row=0, column=0, padx=10, pady=10)

                model = tClient(nif, "Nico", "Alvarez", 20)

                controller = revisionController(model, view)

                view.set_controller(controller)
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def anyadir(self, nif, nombre, apellidos, edad):
        try:
            query = "INSERT INTO tclient VALUES('" + nif + "', '" + nombre + "', '" + apellidos + "', " + str(
                edad) + ");"
            mydb = db(self.url)
            mydb.execute(query)
            self.view.update_refresh()
            print("inserted")
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def selection_changed(self, row):
        self.view.tNIF.delete(0., 'end')
        self.view.tNIF.insert(0., row[0])
        self.view.tNombre.delete(0., 'end')
        self.view.tNombre.insert(0., row[1])
        self.view.tApellidos.delete(0., 'end')
        self.view.tApellidos.insert(0., row[2])
        self.view.list.listEdad.selection_clear(0, 'end')
        self.view.list.listEdad.select_set(row[3] - 1)
        self.view.list.listEdad.see(row[3] - 1)

    def actualizar(self, nif, nombre, apellidos, edad):
        try:
            query = "UPDATE tclient SET NIF='" + nif + "', NOMBRE='" + nombre + "', APELLIDOS='" + apellidos + "', EDAD=" + str(
                edad) + " WHERE NIF = '" + nif + "';"
            mydb = db(self.url)
            mydb.execute(query)
            self.view.update_refresh()
            print("updated")
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def borrar(self, nif):
        try:
            query = "DELETE FROM `mydb`.`tclient` WHERE (`NIF` = '" + str(nif) + "');"
            mydb = db(self.url)
            mydb.execute(query)
            self.view.update_refresh()
            print("deleted")
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def limpiar(self):
        try:
            self.view.datagrid.my_table.selection_remove(self.view.datagrid.my_table.selection()[0])
            self.view.tNIF.delete("1.0", "end")
            self.view.tNombre.delete("1.0", "end")
            self.view.tApellidos.delete("1.0", "end")
            self.view.list.listEdad.selection_clear(0, "end")
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def salir(self, app):
        self.view.destroy()
        app.destroy()
