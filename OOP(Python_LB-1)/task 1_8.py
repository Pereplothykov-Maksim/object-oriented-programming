import unittest

class Product:
    """Клас товару з урахуванням відсоткової знижки."""
    
    def __init__(self, name: str, price: float, discount: float = 0.0):
        if price < 0 or not (0 <= discount <= 100):
            raise ValueError("Некоректна ціна або відсоток знижки.")
        self.name = name
        self.price = price
        self._discount = discount
        
    def final_price(self) -> float:
        """Повертає фінальну ціну з урахуванням знижки."""
        return self.price * (1 - self._discount / 100)
        
    def set_discount(self, p: float) -> None:
        """Встановлює нову знижку в межах від 0 до 100%."""
        if not (0 <= p <= 100):
            raise ValueError("Знижка має бути в межах від 0 до 100%.")
        self._discount = p
        
    def total(self, qty: int) -> float:
        """Обчислює сумарну ціну за qty одиниць товару."""
        if qty < 0:
            raise ValueError("Кількість товару не може бути від'ємною.")
        return self.final_price() * qty

# Демонстрація незалежності даних
p1 = Product("Кава", 100, 10)
p2 = Product("Чай", 50)
print(f"independence Product: final price p1={p1.final_price()}, p2={p2.final_price()}")

# Тести
class TestProduct(unittest.TestCase):
    def test_normal_calculation(self):
        p = Product("Laptop", 1000, 10)
        self.assertEqual(p.final_price(), 900.0)
        self.assertEqual(p.total(2), 1800.0)
        
    def test_boundary_discount(self):
        p = Product("Freebie", 100)
        p.set_discount(100)  # 100% знижка
        self.assertEqual(p.final_price(), 0.0)
        
    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Product("Error", 100, 150)  # Знижка > 100
