class Reporte:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido


class GuardadorReporte:
    def guardar(self, reporte, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(reporte.titulo + "\n" + reporte.contenido)


titulo = input("Título del reporte: ")
contenido = input("Contenido: ")
GuardadorReporte().guardar(Reporte(titulo, contenido), "reporte.txt")
print("Guardado en reporte.txt")