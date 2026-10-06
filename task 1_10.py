import unittest
from typing import List, Optional

# --- Спершу додаємо клас Book, щоб Library могла його бачити ---
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


# --- Тепер іде ваш клас Library ---
class Library:
    """Клас для управління колекцією об'єктів Book."""
    
    def __init__(self):
        self.books: List[Book] = []
        
    def add(self, book: Book) -> None:
        """Додає книгу до бібліотеки."""
        if not isinstance(book, Book):
            raise TypeError("Додати можна лише об'єкт класу Book.")
        self.books.append(book)
        
    def find(self, author: str) -> List[Book]:
        """Повертає список книг заданого автора."""
        return [b for b in self.books if b.author.lower() == author.lower()]
        
    def total_pages(self) -> int:
        """Обчислює сумарну кількість сторінок усіх книг."""
        return sum(b.pages for b in self.books)
        
    def longest(self) -> Optional[Book]:
        """Повертає книгу з найбільшою кількістю сторінок або None, якщо порожньо."""
        return max(self.books, key=lambda b: b.pages) if self.books else None

# Демонстрація незалежності даних
lib1 = Library()
lib2 = Library()
lib1.add(Book("Book A", "Author 1", 100))
print(f"independence Library: Books у lib1={len(lib1.books)}, у lib2={len(lib2.books)}")

# Тести
class TestLibrary(unittest.TestCase):
    def test_normal_flow(self):
        lib = Library()
        b1 = Book("Python Basis", "Guido", 300)
        b2 = Book("Python Advanced", "Guido", 500)
        lib.add(b1)
        lib.add(b2)
        
        self.assertEqual(len(lib.find("Guido")), 2)
        self.assertEqual(lib.total_pages(), 800)
        self.assertEqual(lib.longest(), b2)
        
    def test_boundary_empty_library(self):
        lib = Library()
        self.assertEqual(lib.total_pages(), 0)
        self.assertIsNone(lib.longest())
        self.assertEqual(lib.find("Unknown"), [])
        
    def test_invalid_add(self):
        lib = Library()
        with self.assertRaises(TypeError):
            lib.add("Це просто рядок, не книга")
            
if __name__ == '__main__':
    unittest.main()
