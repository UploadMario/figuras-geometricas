# Este script contiene errores comunes que violan las normas PEP 8
"""Este módulo define clases para representar figuras geométricas y calcular sus áreas."""

from abc import ABC, abstractmethod
class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas."""
    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""

    def descripcion(self):
        """Método para obtener una descripción general de la figura."""
        return f"Figura de tipo {self.__class__.__name__}"

class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo y permite calcular su área."""
    def __init__(self, base , altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        area=self.base*self.altura
        return area

    def calcular_perimetro(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.base + self.altura)


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo y permite calcular su área."""
    def __init__(self, base , altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        area=(self.base*self.altura)/2
        return area

    def calcular_perimetro(self):
        """Cálculo del perímetro del triángulo."""
        # Suponiendo que sea un triángulo equilátero, el perímetro es 3 * base
        return 3 * self.base


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo y permite calcular su área."""
    def __init__(self, radio):
        self.pi =3.14159
        self.radio=radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        area=self.pi*(self.radio**2)
        return area

    def calcular_perimetro(self):
        """Calcula el perímetro del círculo (circunferencia)."""
        return 2 * self.pi * self.radio


# Variables globales
BASE_RECTANGULO =10
ALTURA_RECTANGULO=5
BASE_TRIANGULO=7
ALTURA_TRIANGULO =4
RADIO_CIRCULO =3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO,ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO,ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Cálculo de métodos
    print(f"\n-> Descripción: {rectangulo.descripcion()}")
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El perímetro del rectángulo es: {rectangulo.calcular_perimetro()}")

    print(f"\n-> Descripción {triangulo.descripcion()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El perímetro del triángulo es: {triangulo.calcular_perimetro()}")

    print(f"\n-> Descripción: {circulo.descripcion()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")
    print(f"El perímetro del círculo es: {circulo.calcular_perimetro()}")
