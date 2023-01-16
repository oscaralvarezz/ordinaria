import random 
def main():
    class Stormtrooper():
        def __init__(self):
            self.name = random.choices(['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST'], k=2000)
            self.rango = random.randint(0,2000)
            print('stromtrooper creado con exito!')
    
        

if __name__=='__main__':
    main()