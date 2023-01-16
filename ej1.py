class Nave():
    def __init__(self, codigo, cohoerte, siglo, escuadra, trooper):
        self.codigo = codigo
        self.cohoerte = cohoerte
        self.siglo = siglo
        self.escuadra =escuadra
        self.trooper = trooper

class Stormtrooper(Nave):
    def __init__(self, nombre, rango):
        super().__init__()
        self.nombre = nombre
        self.rango = rango
        print("La clase se ha creado con exito!")

    def calificacion(self):
        codigo_legion = self.codigo
        identificador_coherte = self.cohoerte
        identificador_siglo = self.siglo
        identificador_escuadra = self.escuadra
        numero_trooper = self.trooper
        return f"La nave {self.nombre} tiene los siguientes atributos\nEl codigo de la legion es: {codigo_legion}; El identificador coherte: {identificador_coherte}; El identificador siglo: {identificador_siglo}; El identificador escuadra: {identificador_escuadra}; Numero trooper: {numero_trooper}"


if __name__=="__main__":
    naves = [Nave("Ruben","AK-2890"),Nave("Nave Galactica","DK-0924"),Nave("Nave5","OK-1999")]
    for nave in naves:
        print(f"Nueva nave calificada: {nave.nombre}")
        print(nave.calificacion())