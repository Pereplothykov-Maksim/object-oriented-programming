import unittest

class Student:
    """Клас для збереження даних студента та його оцінок."""
    
    def __init__(self, last_name: str):
        self.last_name = last_name
        self.grades = []
        
    def add_grade(self, g: int) -> None:
        """Додає оцінку від 0 до 100 до списку."""
        if not (0 <= g <= 100):
            raise ValueError("Оцінка повинна бути в межах від 0 до 100.")
        self.grades.append(g)
        
    def average(self) -> float:
        """Повертає середній бал. Якщо оцінок немає — 0.0."""
        return sum(self.grades) / len(self.grades) if self.grades else 0.0
        
    def best(self) -> int:
        """Повертає найкращу оцінку. Якщо оцінок немає — 0."""
        return max(self.grades) if self.grades else 0
        
    def has_debt(self) -> bool:
        """Повертає True, якщо є хоча б одна оцінка нижче 60 балів."""
        return any(g < 60 for g in self.grades) if self.grades else False

# Демонстрація незалежності даних
s1 = Student("Іванов")
s2 = Student("Петров")
s1.add_grade(95)
s2.add_grade(55)
print(f"independence Student: s1 debts? {s1.has_debt()}, s2 debts? {s2.has_debt()}")

# Тести
class TestStudent(unittest.TestCase):
    def test_normal_grades(self):
        s = Student("Smith")
        s.add_grade(80)
        s.add_grade(90)
        self.assertEqual(s.average(), 85.0)
        self.assertEqual(s.best(), 90)
        self.assertFalse(s.has_debt())
        
    def test_boundary_empty_and_debt(self):
        s = Student("NoGrades")
        self.assertEqual(s.average(), 0.0)
        self.assertFalse(s.has_debt())
        s.add_grade(59)
        self.assertTrue(s.has_debt())
        
    def test_invalid_grade(self):
        s = Student("Error")
        with self.assertRaises(ValueError):
            s.add_grade(105)
