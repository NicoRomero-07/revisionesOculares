from db import *
from sqlalchemy import *
from revisionView import revisionView
from revisionController import revisionController
from Modelo.tClient import tClient
import tkinter as tk


class principalController:

    def __init__(self, view):
        self.view = view

    def revisiones(self, nif, app):
        try:
            if nif != "":
                app.title('Revisiones Oculares')
                if len(self.view.datagrid.my_table.selection()) > 0:
                    item = self.view.datagrid.my_table.selection()[0]
                    row = self.view.datagrid.my_table.item(item)['values']
                    nombre = row[1]
                    apellidos = row[2]
                    edad = row[3]
                    view = revisionView(app, nif, nombre, apellidos, edad)
                    view.grid(row=0, column=0, padx=10, pady=10)
                    controller = revisionController(view)
                    view.set_controller(controller)
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def anyadir(self, nif, nombre, apellidos, edad):
        try:
            query = "INSERT INTO tclient VALUES('" + nif + "', '" + nombre + "', '" + apellidos + \
                    "', " + str(edad) + ");"
            mydb = db()
            mydb.execute(query)
            self.view.update_refresh()
            self.limpiar()
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
            query = "UPDATE tclient SET NIF='" + nif + "', NOMBRE='" + nombre + \
                    "', APELLIDOS='" + apellidos + "', EDAD=" + str(
                edad) + " WHERE NIF = '" + nif + "';"
            mydb = db()
            mydb.execute(query)
            self.view.update_refresh()
            self.limpiar()
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def borrar(self, nif):
        try:
            query = "DELETE FROM `mydb`.`tclient` WHERE (`NIF` = '" + str(nif) + "');"
            mydb = db()
            mydb.execute(query)
            self.view.update_refresh()
            self.limpiar()
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def limpiar(self):
        try:
            if len(self.view.datagrid.my_table.selection()) > 0:
                self.view.datagrid.my_table.selection_remove(self.view.datagrid.my_table.selection()[0])
            self.view.tNIF.delete(0.0, "end")
            self.view.tNombre.delete(0.0, "end")
            self.view.tApellidos.delete(0.0, "end")
            self.view.list.listEdad.selection_clear(0, "end")
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def salir(self, app):
        self.view.destroy()
        app.destroy()
