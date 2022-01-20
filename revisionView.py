import tkinter as tk
from tkinter.ttk import *
from tkcalendar import Calendar
from db import *


class revisionView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # create widgets
        # label
        self.label = tk.Label(self, text='Cliente')
        self.label.grid(row=0, column=0, columnspan=6)
        self.label = tk.Label(self, text='OD_Esfera:')
        self.label.grid(row=2, column=0)
        self.label = tk.Label(self, text='OD_Cilindro:')
        self.label.grid(row=3, column=0)
        self.label = tk.Label(self, text='OD_Adicion:')
        self.label.grid(row=4, column=0)
        self.label = tk.Label(self, text='OD_Agudeza:')
        self.label.grid(row=5, column=0)
        self.label = tk.Label(self, text='OI_Esfera:')
        self.label.grid(row=2, column=2)
        self.label = tk.Label(self, text='OI_Cilindro:')
        self.label.grid(row=3, column=2)
        self.label = tk.Label(self, text='OI_Adicion:')
        self.label.grid(row=4, column=2)
        self.label = tk.Label(self, text='OI_Agudeza:')
        self.label.grid(row=5, column=2)
        # email entry
        self.ODEsfera_var = tk.StringVar()
        self.ODEsfera_entry = tk.Entry(self, textvariable=self.ODEsfera_var, width=30)
        self.ODEsfera_entry.grid(row=2, column=1, sticky=tk.NSEW)
        self.ODCilindro_var = tk.StringVar()
        self.ODCilindro_entry = tk.Entry(self, textvariable=self.ODCilindro_var, width=30)
        self.ODCilindro_entry.grid(row=3, column=1, sticky=tk.NSEW)
        self.ODAdicion_var = tk.StringVar()
        self.ODAdicion_entry = tk.Entry(self, textvariable=self.ODAdicion_var, width=30)
        self.ODAdicion_entry.grid(row=4, column=1, sticky=tk.NSEW)
        self.ODAgudeza_var = tk.StringVar()
        self.ODAgudeza_entry = tk.Entry(self, textvariable=self.ODAgudeza_var, width=30)
        self.ODAgudeza_entry.grid(row=5, column=1, sticky=tk.NSEW)

        self.OIEsfera_var = tk.StringVar()
        self.OIEsfera_entry = tk.Entry(self, textvariable=self.OIEsfera_var, width=30)
        self.OIEsfera_entry.grid(row=2, column=3, sticky=tk.NSEW)
        self.OICilindro_var = tk.StringVar()
        self.OICilindro_entry = tk.Entry(self, textvariable=self.OICilindro_var, width=30)
        self.OICilindro_entry.grid(row=3, column=3, sticky=tk.NSEW)
        self.OIAdicion_var = tk.StringVar()
        self.OIAdicion_entry = tk.Entry(self, textvariable=self.OIAdicion_var, width=30)
        self.OIAdicion_entry.grid(row=4, column=3, sticky=tk.NSEW)
        self.OIAgudeza_var = tk.StringVar()
        self.OIAgudeza_entry = tk.Entry(self, textvariable=self.OIAgudeza_var, width=30)
        self.OIAgudeza_entry.grid(row=5, column=3, sticky=tk.NSEW)

        # save button
        self.add_button = tk.Button(self, text='Añadir', command=self.add_button_clicked, height=3, width=10)
        self.add_button.grid(row=7, column=2, padx=20)
        self.actualizar_button = tk.Button(self, text='Actualizar', command=self.actualizar_button_clicked, height=3,
                                           width=10)
        self.actualizar_button.grid(row=7, column=4, padx=20)
        self.borrar_button = tk.Button(self, text='Borrar', command=self.borrar_button_clicked, height=3, width=10)
        self.borrar_button.grid(row=7, column=3, padx=20)
        self.limpiar_button = tk.Button(self, text='Limpiar', command=self.limpiar_button_clicked, height=3, width=10)
        self.limpiar_button.grid(row=8, column=3, padx=20, sticky='w')
        self.salir_button = tk.Button(self, text='Salir', command=self.salir_button_clicked, height=3, width=10)
        self.salir_button.grid(row=8, column=4, padx=20, sticky='w')

        self.label = tk.Label(self, text='\n \n ')
        self.label.grid(row=6, column=2)
        # dataGrid
        self.dataGridFrame = tk.Frame(self)
        revision_scroll = Scrollbar(self.dataGridFrame, orient='horizontal')
        revision_scroll.pack(side='bottom', fill='x')
        self.dataGridFrame.tv = Treeview(self.dataGridFrame, xscrollcommand=revision_scroll.set)
        self.dataGridFrame.tv.pack()

        self.dataGridFrame.grid(row=1, column=0, columnspan=5)
        self.dataGridFrame.tv['columns'] = (
            'revision_id', 'revision_nif', 'revision_consulta', 'revision_od_esfera', 'revision_od_cilindro',
            'revision_od_adicion', 'revision_od_agudeza'
            , 'revision_oi_esfera', 'revision_oi_cilindro', 'revision_oi_adicion', 'revision_oi_agudeza')

        revision_scroll.config(command=self.dataGridFrame.tv.xview)
        self.dataGridFrame.tv.heading("#0", text="", anchor='center')
        self.dataGridFrame.tv.column("#0", anchor='center', width=1)
        self.dataGridFrame.tv.heading("revision_id", text="Id")
        self.dataGridFrame.tv.column("revision_id", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_nif", text="NIF", anchor='center')
        self.dataGridFrame.tv.column("revision_nif", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_consulta", text="Consulta", anchor='center')
        self.dataGridFrame.tv.column("revision_consulta", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_od_esfera", text="OD_Esfera", anchor='center')
        self.dataGridFrame.tv.column("revision_od_esfera", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_od_cilindro", text="OD_Cilindro", anchor='center')
        self.dataGridFrame.tv.column("revision_od_cilindro", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_od_adicion", text="OD_Adicion", anchor='center')
        self.dataGridFrame.tv.column("revision_od_adicion", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_od_agudeza", text="OD_Agudeza", anchor='center')
        self.dataGridFrame.tv.column("revision_od_agudeza", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_oi_esfera", text="OI_Esfera", anchor='center')
        self.dataGridFrame.tv.column("revision_oi_esfera", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_oi_cilindro", text="OI_Cilindro", anchor='center')
        self.dataGridFrame.tv.column("revision_oi_cilindro", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_oi_adicion", text="OI_Adicion", anchor='center')
        self.dataGridFrame.tv.column("revision_oi_adicion", anchor='center', width=100)
        self.dataGridFrame.tv.heading("revision_oi_agudeza", text="OI_Agudeza", anchor='center')
        self.dataGridFrame.tv.column("revision_oi_agudeza", anchor='center', width=100)


        # Calendario
        self.selected_date = tk.StringVar()

        self.cal = Calendar(self, selectmode='day',
                            year=2020, month=5,
                            day=22, textvariable= self.selected_date)
        self.cal.grid(row=7, column=0, columnspan=2, rowspan=2)

        self.update_refresh()

        self.dataGridFrame.tv.bind("<<TreeviewSelect>>", self.selection_changed)
        # set the controller
        self.controller = None


    def selection_changed(self, x):
        if self.controller:
            if len(self.dataGridFrame.tv.selection()) > 0:
                item = self.dataGridFrame.tv.selection()[0]
                row = self.dataGridFrame.tv.item(item)['values']
                self.controller.selection_changed(row)

    def update_refresh(self):
        # url = 'mysql+pymysql://root:nicolaszhiliezhao@localhost:3306/mydb'
        url = 'mysql://root:1234@localhost:3306/mydb'
        mydb = db(url)
        query = "SELECT * FROM teye"
        rows = mydb.query(query)
        self.update_datagrid(rows)

    def update_datagrid(self, rows):
        for i in self.dataGridFrame.tv.get_children():
            self.dataGridFrame.tv.delete(i)
        for i in rows:
            self.dataGridFrame.tv.insert('', 'end', values=(i['ID'], i['NIF'], i['CONSULTA'], i['OD_ESFERA'],
                                                            i['OD_CILINDRO'],i['OD_ADICION'],i['OD_AGUDEZA'],
                                                            i['OI_ESFERA'],i['OI_CILINDRO'],i['OI_ADICION'],i['OI_AGUDEZA']))
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def add_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.add(self.controller.model.NIF , self.cal.get_date(), self.ODEsfera_var.get(), self.ODCilindro_var.get(), self.ODAdicion_var.get(),
                                self.OIAgudeza_var.get(), self.OIEsfera_var.get(), self.OICilindro_var.get(),
                                self.OIAdicion_var.get(), self.OIAgudeza_var.get())

    def actualizar_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.actualizar(self.ODEsfera_var.get(), self.ODCilindro_var.get(), self.ODAdicion_var.get(),
                                       self.OIAgudeza_var, self.OIEsfera_var.get(), self.OICilindro_var.get(),
                                       self.OIAdicion_var.get(), self.OIAgudeza_var)

    def borrar_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.borrar(self.ODEsfera_var.get(), self.ODCilindro_var.get(), self.ODAdicion_var.get(),
                                   self.OIAgudeza_var, self.OIEsfera_var.get(), self.OICilindro_var.get(),
                                   self.OIAdicion_var.get(), self.OIAgudeza_var)

    def limpiar_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.limpiar(self.ODEsfera_var.get(), self.ODCilindro_var.get(), self.ODAdicion_var.get(),
                                    self.OIAgudeza_var, self.OIEsfera_var.get(), self.OICilindro_var.get(),
                                    self.OIAdicion_var.get(), self.OIAgudeza_var)

    def salir_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.salir(self.parent)

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''
