from abc import ABC, abstractmethod

class Impresora(ABC):
    @abstractmethod
    def imprimir(self): pass

class Escaner(ABC):
    @abstractmethod
    def escanear(self): pass

class ImpresoraSencilla(Impresora):
    def imprimir(self):
        print("Imprimiendo documento...")

class Multifuncional(Impresora, Escaner):
    def imprimir(self):
        print("Imprimiendo documento...")
    def escanear(self):
        print("Escaneando documento...")


opcion = input("¿Qué acción? (1 = imprimir, 2 = escanear): ")
if opcion == "1":
    ImpresoraSencilla().imprimir()
else:
    Multifuncional().escanear()