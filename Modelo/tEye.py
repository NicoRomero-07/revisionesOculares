from typing import Any

from Modelo.tClient import tClient


class tEye(tClient):

    def __init__(self,tClient,NIF,consulta,od_esfera,od_cilindro,od_adicion,od_agudeza,oi_esfera,oi_cilindro,oi_adicion,oi_agudeza):
        self.__tClient = tClient
        self.__NIF = NIF
        self.__consulta = consulta
        self.__od_esfera = od_esfera
        self.__od_cilindro = od_cilindro
        self.__od_adicion = od_adicion
        self.__od_agudeza = od_agudeza
        self.__oi_esfera = oi_esfera
        self.__oi_cilindro = oi_cilindro
        self.__oi_adicion = oi_adicion
        self.__oi_agudeza = oi_agudeza


    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

