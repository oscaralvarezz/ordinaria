class Stormtrooper():
        def __init__(self, name, rango):
            self.name = name
            self.rango = rango
            self.calificacion()
            print('Se ha creado un stromtrooper con éxito!')
        
        def __str__(self):
            return 'Stormtrooper: {} con rango {} y calificacion: {}'.format(self.name, self.rango, self.calificacion)

        def calificacion(self):
            for i in self.name:
                if self.name == 'TK':
                    print('{}código de legión {}'.format(self.name, self.rango))
                if self.name == '8':
                    print('{}identificador coherente{}'.format(self.name, self.rango))
                if self.name == '6':
                    print('{}identificador de siglo {}'.format(self.name, self.rango))
                if self.name == '5':
                    print('{} tiene un número de trooper {}'.format(self.name, self.rango))
                if self.name == '4':
                    print('{}identificador de escuadra{}'.format(self.name, self.rango))

Trooper1 = Stormtrooper('TK-421', 10)
Trooper2 = Stormtrooper('8-8-8', 10)
Trooper3 = Stormtrooper('6-6-6', 10)
Lista = [Trooper1, Trooper2, Trooper3]
#mostramos por pantalla el Trooper1
print(Trooper1)

#for i in Lista:
    #print(i)