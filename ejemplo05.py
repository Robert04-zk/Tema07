from abc import ABC, abstractmethod

class ServicioMensaje(ABC):
    @abstractmethod
    def enviar(self, msg): pass

class ServicioSMS(ServicioMensaje):
    def enviar(self, msg):
        print("SMS:", msg)

class ServicioEmail(ServicioMensaje):
    def enviar(self, msg):
        print("Email:", msg)

class Notificador:
    def __init__(self, servicio):
        self.servicio = servicio
    def enviar_alerta(self, msg):
        self.servicio.enviar(msg)


mensaje = input("Mensaje: ")
canal = input("Canal (sms / email): ").lower()
servicio = ServicioSMS() if canal == "sms" else ServicioEmail()
Notificador(servicio).enviar_alerta(mensaje)