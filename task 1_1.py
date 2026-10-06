import math
import unittest

class Point:
    """Клас, що представляє точку на двовимірній площині (x, y)."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)
        
    def distance_to(self, other: 'Point') -> float:
        """Обчислює відстань до іншої точки other."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        
    def move(self, dx: float, dy: float) -> None:
        """Зсуває точку на задані значення dx та dy."""
        self.x += dx
        self.y += dy
        
    def is_origin(self) -> bool:
        """Перевіряє, чи знаходиться точка на початку координат (0, 0)."""
        return math.isclose(self.x, 0.0) and math.isclose(self.y, 0.0)

# Демонстрація незалежності даних
p1 = Point(0, 0)
p2 = Point(3, 4)
p1.move(1, 1)  # p1 змістився, p2 залишився без змін
print(f"Незалежність Point: p1({p1.x}, {p1.y}), p2({p2.x}, {p2.y})")

# Тести
class TestPoint(unittest.TestCase):
    def test_normal_case(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertEqual(p1.distance_to(p2), 5.0)
        
    def test_boundary_case(self):
        p = Point(0, 0)
        self.assertTrue(p.is_origin())
        p.move(0.0000001, 0)
        self.assertFalse(p.is_origin())
        
    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Point("abc", 0)
