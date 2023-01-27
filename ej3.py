class ElementosValiosos():
        def __init__(self, peso, nombre, precio, caducidad):
            self.peso = peso
            self.nombre = nombre
            self.precio = precio
            self.caducidad = caducidad
            print('Un Artefacto Valioso se ha creado con exito!')
        
        def __str__(self):
            return 'El Artefacto Valioso: {} con un peso de {} Kg, un precio de: {} euros, y una fecha de caducidad: {}'.format(self.nombre, self.peso, self.precio, self.caducidad)
        
#Asignamos los valores y características de los elementos.
elemento1= ElementosValiosos(10, 'Artefacto 1', 50, '01/07/2020')
elemento2= ElementosValiosos(20, 'Artefacto 2', 600, '01/09/2020')
elemento3= ElementosValiosos(30, 'Artefacto 3', 30, '01/08/2020')

Lista = [elemento1, elemento2, elemento3]
for i in Lista: 
    print(i)

    #ordenamos la lista que hemos creado anteriormente.
    def ordenar_lista(Lista):
        Lista.sort(key=lambda x: x.caducidad)
        print(Lista)
    ordenar_lista(Lista)

    #finalmente, creamos una función que nos permita cambiar el precio de un elemento
    def cambiar_precio(elemento, nuevo_precio):
        elemento.precio = nuevo_precio
        print('{} con nuevo precio de: {} euros'.format(elemento.nombre, elemento.precio))
    
    cambiar_precio(elemento1, 2000)