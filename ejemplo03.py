class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Volando..."

class Pinguino(Ave):
    def nadar(self):
        return "Nadando..."


opcion = input("¿Qué ave? (1 = Aguila, 2 = pingino): ")
if opcion == "1":
    print(AveVoladora().volar())
else:
    print(Pinguino().nadar())