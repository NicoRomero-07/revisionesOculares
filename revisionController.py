from datetime import datetime

from sqlalchemy import create_engine, null
from sqlalchemy import text

import principalController as pC
import principalView as pV

from Modelo.tClient import tClient
from db import db


class revisionController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def selection_changed(self, row):
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

    def selectMaxId(self):
        query = "SELECT COUNT(ID) FROM teye"
        mydb = db()
        rows = mydb.query(query)
        return rows[0]['COUNT(ID)']


    def add(self, nif, fecha, OD_Esfera, OD_Cilindro, OD_Adicion, OD_Agudeza, OI_Esfera, OI_Cilindro, OI_Adicion,
            OI_Agudeza):

        try:

            id = self.selectMaxId()
            print(id)
            print(str(fecha))
            query = "INSERT INTO teye  (`ID`, `NIF`, `CONSULTA`, `OD_ESFERA`, `OD_CILINDRO`, `OD_ADICION`, `OD_AGUDEZA`, `OI_ESFERA`, `OI_CILINDRO`, `OI_ADICION`, `OI_AGUDEZA`) VALUES("+ str(id + 1) + ",'" + nif + "', '" + str(fecha) + "', " + str(OD_Esfera)  +", "+ str(OD_Cilindro) +", "+  str(OD_Adicion) + ", "+ str(OD_Agudeza) + ", " + str(OI_Esfera) + ", " + str(OI_Cilindro) + ", " + str( OI_Adicion) + ", " + str(OI_Agudeza) +");"
            mydb = db()
            mydb.execute(query)
            self.view.update_refresh()
            self.limpiar()
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def borrar(self):
        try:
            if self.view.dataGridFrame.tv.selection()[0] != null:
                item = self.view.dataGridFrame.tv.selection()[0]
                row = self.view.dataGridFrame.tv.item(item)['values']
                cellValue = row[0]
                query = "DELETE FROM mydb.teye WHERE (ID = " + str(cellValue) + ");"
                mydb = db()
                mydb.execute(query)
                self.view.update_refresh()
                self.limpiar()

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def actualizar(self, Consulta, OD_Esfera, OD_Cilindro, OD_Adicion, OD_Agudeza, OI_Esfera, OI_Cilindro, OI_Adicion,
                   OI_Agudeza):

        try:
            if self.view.dataGridFrame.tv.selection()[0] != null:
                item = self.view.dataGridFrame.tv.selection()[0]
                row = self.view.dataGridFrame.tv.item(item)['values']
                cellValue = row[0]
            query = "UPDATE teye SET  CONSULTA='" + str(Consulta) + "', OD_ESFERA=" + str(OD_Esfera) + ", OD_CILINDRO=" + str(OD_Cilindro) + ", OD_ADICION="+str(OD_Adicion) +", OD_Agudeza="+str(OD_Agudeza)+", OI_ESFERA=" + str(OI_Esfera) + ", OI_CILINDRO=" + str(OI_Cilindro) + ", OI_ADICION="+str(OI_Adicion) +" ,OI_Agudeza="+str(OI_Agudeza)+" WHERE ID = '" + str(cellValue) + "';"
            mydb = db()
            mydb.execute(query)
            self.view.update_refresh()
            self.limpiar()

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def limpiar(self):

        try:
            if len(self.view.dataGridFrame.tv.selection()) > 0:
                self.view.dataGridFrame.tv.selection_remove(self.view.dataGridFrame.tv.selection()[0])
            self.view.ODEsfera_entry.delete(0, 'end')
            self.view.ODCilindro_entry.delete(0, 'end')
            self.view.ODAdicion_entry.delete(0, 'end')
            self.view.ODAgudeza_entry.delete(0, 'end')
            self.view.OIEsfera_entry.delete(0, 'end')
            self.view.OICilindro_entry.delete(0, 'end')
            self.view.OIAdicion_entry.delete(0, 'end')
            self.view.OIAgudeza_entry.delete(0, 'end')
            self.view.cal.selection_set(datetime.today())

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
