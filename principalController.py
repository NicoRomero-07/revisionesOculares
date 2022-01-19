from db import *

class principalController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.url = 'mysql://nicor:1234@localhost:3306/mydb'

    def revisiones(self, nif, nombre, apellidos, edad):
        try:
            2
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def anyadir(self, nif, nombre, apellidos, edad):
        try:
            query = "INSERT INTO tclient VALUES('" + nif + "', '" + nombre + "', '"\
                    + apellidos + "', " + str(edad) + ");"
            mydb = db(self.url)
            mydb.execute(query)
            self.view.update_refresh()
            print("inserted")
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def actualizar(self, nif, nombre, apellidos, edad):
        try:
            query = "UPDATE tclient " \
                    "SET NIF='" + nif + "', NOMBRE='" + nombre + \
                    "', APELLIDOS='" + apellidos + "', EDAD=" + str(edad) + \
                    "WHERE NIF = '"+nif+"';"
            mydb = db(self.url)
            mydb.execute(query)
            self.view.update_refresh()
            print("updated")
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def borrar(self, nif):
        try:
            query = "DELETE * FROM tclient WHERE NIF = '"+nif+"';"
            mydb = db(self.url)
            mydb.execute(query)
            self.view.update_refresh()
            print("deleted")
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def limpiar(self):
        try:
            self.view.datagrid.my_table.selection_clear()
            self.view.tNIF.delete("1.0", "end")
            self.view.tNombre.delete("1.0", "end")
            self.view.tApellidos.delete("1.0", "end")
            self.view.list.listEdad.selection_clear("end")
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def salir(self):
        self.view.destroy()
