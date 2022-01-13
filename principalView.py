import tkinter as ttk
from tkinter.ttk import *
class principalView (ttk.Frame):

    def __init__(self,parent):
        super().__init__(parent)

        self.title = ttk.Label(self, text="Revisión Ocular")
        self.title.config (font=('Helvetica bold',25))
        self.title.grid(row = 0,column=1,padx=10,pady=10,columnspan=4)

        self.labelNIF = ttk.Label(self, text="NIF")
        self.labelNIF.grid(row = 2,column=2,pady=10)
        self.labelNombre = ttk.Label(self, text="Nombre")
        self.labelNombre.grid(row = 3, column=2, pady=10)
        self.labelApellidos = ttk.Label (self, text="Apellidos")
        self.labelApellidos.grid(row = 4, column=2, pady=10)
        self.labelEdad = ttk.Label (self, text="Edad")
        self.labelEdad.grid(row = 5, column=2 ,pady=10)
        self.tNIF = ttk.Text(self,height = 1,width= 30)
        self.tNIF.grid(row = 2,column = 2,padx=10,pady=10,columnspan=4)
        self.tNombre = ttk.Text(self,height = 1,width= 30)
        self.tNombre.grid(row=3, column=2, padx=10,pady=10,columnspan=4)
        self.tApellidos = ttk.Text(self,height = 1,width= 30)
        self.tApellidos.grid(row=4, column=2, padx=10,pady=10,columnspan=4)

        #Button
        self.bRevisiones = ttk.Button(self,height=2,width= 14, text="Revisiones",command=self.revisiones_button_clicked)
        self.bRevisiones.grid(row=5, column=4, padx=10, pady=20)
        self.bAnyadir = ttk.Button (self,height=1,width= 10, text="Añadir",command=self.anyadir_button_clicked)
        self.bAnyadir.grid(row=6,column=1,padx=10,pady=20)
        self.bActualizar = ttk.Button(self, height=1, width=10, text="Actualizar",command=self.actualizar_button_clicked)
        self.bActualizar.grid(row=6, column=2,padx=10,pady=20)
        self.bBorrar = ttk.Button(self, height=1, width=10, text="Borrar",command=self.borrar_button_clicked)
        self.bBorrar.grid(row=6, column=3,padx=10,pady=20)
        self.bLimpiar = ttk.Button(self, height=1, width=10, text="Limpiar",command=self.limpiar_button_clicked)
        self.bLimpiar.grid(row=6, column=4,padx=10,pady=20)
        self.bSalir = ttk.Button(self, height=1, width=10, text="Salir",command=self.salir_button_clicked)
        self.bSalir.grid(row=6, column=5,padx=10,pady=20)



        #ListBox
        list = ttk.Frame(self)
        scroll = ttk.Scrollbar(list)
        scroll.pack(side="right", fill="y")
        self.listEdad = ttk.Listbox(list,height = 3,width= 15)
        scroll.config(command=self.listEdad.yview)
        self.listEdad.pack()
        list.grid(row=5,column=3,padx=10,pady=10)


        #Datagrid
        # scrollbar
        datagrid = ttk.Frame(self)

        scroll = ttk.Scrollbar(datagrid)
        scroll.pack(side="right", fill="y")

        scroll = ttk.Scrollbar(datagrid, orient='horizontal')
        scroll.pack(side="bottom", fill="x")

        my_table = Treeview(datagrid, yscrollcommand=scroll.set, xscrollcommand=scroll.set)
        my_table.pack()

        datagrid.grid(row = 1, column = 2, padx=10, pady=10,columnspan=3)


        # define our column

        my_table['columns'] = ('NIF', 'NOMBRE', 'APELLIDOS', 'EDAD')

        # format our column
        my_table.column("#0", width=0, stretch="NO")
        my_table.column("NIF", anchor="center", width=80)
        my_table.column("NOMBRE", anchor="center", width=80)
        my_table.column("APELLIDOS", anchor="center", width=80)
        my_table.column("EDAD", anchor="center", width=80)

        # Create Headings
        my_table.heading("#0", text="", anchor="center")
        my_table.heading("NIF", text="Id", anchor="center")
        my_table.heading("NOMBRE", text="Name", anchor="center")
        my_table.heading("APELLIDOS", text="Rank", anchor="center")
        my_table.heading("EDAD", text="States", anchor="center")

    def set_controller(self, controller):
        self.controller = controller

    def salir_button_clicked(self):
        if self.controller:
            self.controller.salir()

    def limpiar_button_clicked(self):
        if self.controller:
            self.controller.limpiar()

    def anyadir_button_clicked(self):
        2
    def borrar_button_clicked(self):
        2
    def revisiones_button_clicked(self):
        2
    def actualizar_button_clicked(self):
        2