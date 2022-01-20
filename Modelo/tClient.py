from typing import Any


class tClient:

    def __init__(self, NIF, nombre, apellidos, edad):
        self.NIF = NIF
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return "NIF= " + self.__NIF + " nombre= " + self.__nombre + " apellidos " + self.__apellidos, self.__edad
