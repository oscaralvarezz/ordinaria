class Artefactosvaliosos():
    def __init__(self, peso, nombre, precio, caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.caducidad = caducidad
        print("La conserva se ha creado con exito!")

    def __str__(self):
        return f"Las caracteristicas de los productos son:\n - Peso: {self.peso}\n - Nombre: {self.nombre}\n - Precio: {self.precio}\n - Caducidad: {self.caducidad}"

if __name__=="__main__":
    artefactos = [Artefactosvaliosos(100,"David",1500,"28-08-2090"), Artefactosvaliosos(100,"Carmen",14,"30-08-2190"),Artefactosvaliosos(150,"Enrique",1590,"02-08-2090")]
    
    artefactos.sort(key=lambda x: x.caducidad)
    
    for artefacto in artefactos:
        print(artefacto)