class Descuento:
    def aplicar(self, precio):
        return precio

class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.8

class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.9


tipos = {"vip": DescuentoVIP(), "estudiante": DescuentoEstudiante()}

precio = float(input("Precio: "))
cliente = input("Cliente (vip / estudiante / otro): ").lower()
descuento = tipos.get(cliente, Descuento())
print("Total a pagar: S/", round(descuento.aplicar(precio), 2))