class principalController:

    def __init__(self,view):
        self.view = view

    #def revisiones(self,nif,nombre,apellidos,edad):


    #def anyadir(self,nif,nombre,apellidos,edad):

    #def actualizar(self,nif,nombre,apellidos,edad):

    #def borrar(self,nif,nombre,apellidos,edad):

    def limpiar(self):
        self.view.datagrid.my_table.selection_clear()
        self.view.tNIF.delete("start", "end")
        self.view.tNombre.delete("start", "end")
        self.view.tApellidos.delete("start", "end")
        self.view.list.listEdad.selection_clear()

    def salir(self):
        self.view.destroy()

