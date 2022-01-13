from sqlalchemy import create_engine
from sqlalchemy import text


class revisionController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

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
            2+2

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def salir(self, OD_Esfera, OD_Cilindro, OD_Adicion, OD_Agudeza, OI_Esfera, OI_Cilindro, OI_Adicion, OI_Agudeza):

        try:
            2+2

        except ValueError as error:
            # show an error message
            self.view.show_error(error)
