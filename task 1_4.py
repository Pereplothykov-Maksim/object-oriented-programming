import unittest

class Book:
    """Клас, що описує книгу та прогрес її читання."""
    
    def __init__(self, title: str, author: str, pages: int):
        if pages <= 0:
            raise ValueError("Кількість сторінок має бути додатною.")
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        
    def read(self, n: int) -> None:
        """Додає n прочитаних сторінок, але не далі останньої сторінки."""
        if n < 0:
            raise ValueError("Не можна читати від'ємну кількість сторінок.")
        self.current_page = min(self.current_page + n, self.pages)
        
    def progress(self) -> float:
        """Повертає відсоток прочитаного від 0.0 до 100.0."""
        return (self.current_page / self.pages) * 100
        
    def is_finished(self) -> bool:
        """Перевіряє, чи книга прочитана до кінця."""
        return self.current_page == self.pages

# Демонстрація незалежності даних
b1 = Book("1984", "Orwell", 300)
b2 = Book("Dune", "Herbert", 600)
b1.read(150)
print( " findependence Book: b1 progress={b1.progress()}%, b2 progress={b2.progress()}%")

# Тести
class TestBook(unittest.TestCase):
    def test_normal_reading(self):
        b = Book("Test", "Author", 100)
        b.read(20)
        self.assertEqual(b.progress(), 20.0)
        self.assertFalse(b.is_finished())
        
    def test_boundary_finish(self):
        b = Book("Test", "Author", 100)
        b.read(150)  # Спроба прочитати більше, ніж є сторінок
        self.assertEqual(b.current_page, 100)
        self.assertTrue(b.is_finished())
        
    def test_invalid_pages(self):
        with self.assertRaises(ValueError):
            Book("Fail", "Author", -5)
