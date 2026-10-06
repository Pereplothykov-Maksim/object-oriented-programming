import unittest

class Car:
    """Клас, що симулює роботу паливної системи автомобіля."""
    
    def __init__(self, brand: str, tank_capacity: float, consumption: float):
        if tank_capacity <= 0 or consumption <= 0:
            raise ValueError("Параметри бака та витрати мають бути додатними.")
        self.brand = brand
        self.tank_capacity = tank_capacity
        self.fuel_level = 0.0
        self.consumption = consumption  # на 100 км
        
    def refuel(self, l: float) -> None:
        """Заправляє авто на l літрів, але не більше місткості бака."""
        if l < 0:
            raise ValueError("Не можна заправити від'ємну кількість літрів.")
        self.fuel_level = min(self.fuel_level + l, self.tank_capacity)
        
    def drive(self, km: float) -> float:
        """Їде на відстань km. Повертає фактично пройдену дистанцію."""
        if km < 0:
            raise ValueError("Відстань не може бути від'ємною.")
        max_distance = (self.fuel_level / self.consumption) * 100
        
        if km <= max_distance:
            self.fuel_level -= (km * self.consumption) / 100
            return km
        else:
            self.fuel_level = 0.0
            return max_distance
            
    def range_left(self) -> float:
        """Повертає залишкову відстань, яку авто здатне проїхати на залишку пального."""
        return (self.fuel_level / self.consumption) * 100

# Демонстрація незалежності даних
car1 = Car("Audi", 60, 8)
car2 = Car("Fiat", 40, 5)
car1.refuel(20)
print(f"independence Car: range car1={car1.range_left()} км, car2={car2.range_left()} км")

# Тести
class TestCar(unittest.TestCase):
    def test_normal_drive(self):
        c = Car("Ford", 50, 10)  # 10л на 100км (1л на 10км)
        c.refuel(20)
        fact_dist = c.drive(50)
        self.assertEqual(fact_dist, 50)
        self.assertEqual(c.fuel_level, 15.0)
        
    def test_boundary_empty_tank(self):
        c = Car("Ford", 50, 10)
        c.refuel(5)  # Вистачить на 50 км
        fact_dist = c.drive(200)  # Спроба проїхати більше
        self.assertEqual(fact_dist, 50.0)
        self.assertEqual(c.fuel_level, 0.0)
        
    def test_invalid_refuel(self):
        c = Car("Tesla", 50, 1)
        with self.assertRaises(ValueError):
            c.refuel(-10)
