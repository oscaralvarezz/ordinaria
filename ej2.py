class Stormtrooper():
        def __init__(self, name, rango):
            self.name = name
            self.rango = rango
            self.calificacion()
            print('stromtrooper creado con exito!')
        
        def __str__(self):
            return 'Stormtrooper: {} con rango {} y calificacion: {}'.format(self.name, self.rango, self.calificacion)

        def calificacion(self):
            for i in self.name:
                if self.name == 'TK':
                    print('{}codigo de legion {}'.format(self.name, self.rango))
                if self.name == '8':
                    print('{}identificador coherente{}'.format(self.name, self.rango))
                if self.name == '6':
                    print('{}identificador de siglo {}'.format(self.name, self.rango))
                if self.name == '5':
                    print('{} tiene un numero de trooper {}'.format(self.name, self.rango))
                if self.name == '4':
                    print('{}identificador de escuadra{}'.format(self.name, self.rango))

trooper1 = Stormtrooper('TK-421', 10)
trooper2 = Stormtrooper('8-8-8', 10)
trooper3 = Stormtrooper('6-6-6', 10)
lista = [trooper1, trooper2, trooper3]
print(trooper1)

for i in lista:
    print(i)