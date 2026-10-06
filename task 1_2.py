import math
import unittest

class Rectangle:
    """Клас для роботи з прямокутником за шириною та висотою."""
    
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Розміри прямокутника мають бути більшими за нуль.")
        self.width = width
        self.height = height
        
    def area(self) -> float:
        """Повертає площу прямокутника."""
        return self.width * self.height
        
    def perimeter(self) -> float:
        """Повертає периметр прямокутника."""
        return 2 * (self.width + self.height)
        
    def is_square(self) -> bool:
        """Перевіряє, чи є прямокутник квадратом."""
        return math.isclose(self.width, self.height)

# Демонстрація незалежності даних
r1 = Rectangle(4, 4)
r2 = Rectangle(5, 10)
print(f"independence  Rectangle: r1 square? {r1.is_square()}, r2 square?  {r2.is_square()}")

# Тести
class TestRectangle(unittest.TestCase):
    def test_normal(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)
        self.assertEqual(r.perimeter(), 18)
        
    def test_boundary_square(self):
        r = Rectangle(5.5, 5.5)
        self.assertTrue(r.is_square())
        
    def test_invalid(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)
