from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import text

import principalController as pC
import principalView as pV

from Modelo.tClient import tClient


class revisionController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def selection_changed(self, row):
        formato = format(row[2])
        print(str(row[2]))
        print(formato)
        print(datetime.strptime(str(row[2]), '%Y-%m-%d'))
        self.view.cal.selection_set(datetime.strptime(str(row[2]), '%Y-%m-%d'))
        self.view.ODEsfera_entry.delete(0, 'end')
        self.view.ODEsfera_entry.insert(0, row[3])
        self.view.ODCilindro_entry.delete(0, 'end')
        self.view.ODCilindro_entry.insert(0, row[4])
        self.view.ODAdicion_entry.delete(0, 'end')
        self.view.ODAdicion_entry.insert(0, row[5])
        self.view.ODAgudeza_entry.delete(0, 'end')
        self.view.ODAgudeza_entry.insert(0, row[6])
        self.view.OIEsfera_entry.delete(0, 'end')
        self.view.OIEsfera_entry.insert(0, row[7])
        self.view.OICilindro_entry.delete(0, 'end')
        self.view.OICilindro_entry.insert(0, row[8])
        self.view.OIAdicion_entry.delete(0, 'end')
        self.view.OIAdicion_entry.insert(0, row[9])
        self.view.OIAgudeza_entry.delete(0, 'end')
        self.view.OIAgudeza_entry.insert(0, row[10])


    def add(self, OD_Esfera, OD_Cilindro, OD_Adicion, OD_Agudeza, OI_Esfera, OI_Cilindro, OI_Adicion, OI_Agudeza):

        try:
            print("add")
            engine = create_engine('mysql://nicor:1234@localhost:3306/mydb')
            with engine.connect() as conn:
                result = conn.execute(text("select 'hello world'"))
                print(result.all())
            
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def borrar(self, OD_Esfera, OD_Cilindro, OD_Adicion, OD_Agudeza, OI_Esfera, OI_Cilindro, OI_Adicion, OI_Agudeza):

        try:
            2+2

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def actualizar(self, OD_Esfera, OD_Cilindro, OD_Adicion, OD_Agudeza, OI_Esfera, OI_Cilindro, OI_Adicion, OI_Agudeza):

        try:
            2+2

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def limpiar(self, OD_Esfera, OD_Cilindro, OD_Adicion, OD_Agudeza, OI_Esfera, OI_Cilindro, OI_Adicion, OI_Agudeza):

        try:
            self.view.dataGridFrame.tv.selection_remove(self.view.dataGridFrame.tv.selection()[0])
            self.view.tNIF.delete("1.0", "end")
            self.view.tNombre.delete("1.0", "end")
            self.view.tApellidos.delete("1.0", "end")
            self.view.list.listEdad.selection_clear(0, "end")

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def salir(self, app):
        try:
            self.view.destroy()
            app.title('Revisiones Oculares')

            view = pV.principalView(app)
            view.grid(row=0, column=0, padx=10, pady=10)

            model = tClient(1, "Nico", "Alvarez", 20)

            controller = pC.principalController(model, view)
            view.set_controller(controller)
        except ValueError as error:
            # show an error message
            self.view.show_error(error)
