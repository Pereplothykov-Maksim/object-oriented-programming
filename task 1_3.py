import unittest

class Counter:
    """Клас-лічильник цілих невід'ємних чисел."""
    
    def __init__(self):
        self._value = 0
        
    def increment(self) -> None:
        """Збільшує лічильник на 1."""
        self._value += 1
        
    def decrement(self) -> None:
        """Зменшує лічильник на 1, але не нижче 0."""
        if self._value > 0:
            self._value -= 1
            
    def reset(self) -> None:
        """Скидає лічильник до нуля."""
        self._value = 0
        
    def value(self) -> int:
        """Повертає поточне значення лічильника."""
        return self._value

# Демонстрація незалежності даних
c1 = Counter()
c2 = Counter()
c1.increment()
print(f"independence  Counter: c1={c1.value()}, c2={c2.value()}")

# Тести
class TestCounter(unittest.TestCase):
    def test_normal(self):
        c = Counter()
        c.increment()
        c.increment()
        self.assertEqual(c.value(), 2)
        
    def test_boundary_decrement(self):
        c = Counter()
        c.decrement()  # Спроба опуститися нижче 0
        self.assertEqual(c.value(), 0)
        
    def test_reset(self):
        c = Counter()
        c.increment()
        c.reset()
        self.assertEqual(c.value(), 0)
