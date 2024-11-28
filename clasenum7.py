"""Configura un entorno de pruebas local para tu proyecto usando pytest. 
Escribe una prueba sencilla que verifique que la función sumar(a, b) 
devuelve la suma correcta de dos números."""

class suma:
    def __init__(self):
        self.resultado=0

    def sumar(self,num1,num2):
        self.resultado=num1+num2
        return self.resultado    
    