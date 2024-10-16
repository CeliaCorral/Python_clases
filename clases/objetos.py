# Clases en python
# OOP -> 

# Estudiante -> Persona: sí; 
genero = ''
cien_pesos = 100
class Persona:
    genero = ''
    def __init__(self, nombre: str, edad: int, estatura: float) -> None: # Dunder -> double underscore
        genero = ''
        # Metodos magics
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura

    def __str__(self):
        return f'La persona se llama {self.nombre} de edad: {self.edad} y estatura: {self.estatura}'

    def representacion_en_cadena(self):
        return f'La persona se llama {self.nombre} de edad: {self.edad} y estatura: {self.estatura}'


persona_1 = Persona("Celia", 20, 1.61)
print(persona_1)
print(persona_1.representacion_en_cadena())
print(f"La persona se llama {persona_1.nombre} de edad: {persona_1.edad} y estatura: {persona_1.estatura}") # No recomendado

# Concepto de herencia

class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, estatura: float, salario: float) -> None:
        super().__init__(nombre, edad, estatura)
        self.salario = salario
    def __str__(self):
        return f'La persona se llama {self.nombre} de edad: {self.edad} y estatura: {self.estatura}. Percibe un salario {self.salario}'



#       A
# B.           C
#E M          Q P
empleado_1 = Empleado("Celia", 20, 1.61, 100000.00)
print(empleado_1)

print(persona_1.edad + cien_pesos)
print(empleado_1.salario + cien_pesos)

# polimorfismo
class C:
    pass

class B:
    pass
class A(B, C): # SOLID 

    pass  # Single Responsibility

# encapsulamiento 

# SOLID 