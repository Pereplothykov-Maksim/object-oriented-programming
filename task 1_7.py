import unittest
from typing import Optional

class Stack:
    """Клас, що реалізує структуру даних Стек (LIFO) для цілих чисел."""
    
    def __init__(self):
        self._items = []
        
    def push(self, x: int) -> None:
        """Додає ціле число на вершину стека."""
        if not isinstance(x, int):
            raise TypeError("Стек приймає лише цілі числа.")
        self._items.append(x)
        
    def pop(self) -> Optional[int]:
        """Видаляє та повертає елемент з вершини. Повертає None, якщо порожній."""
        return self._items.pop() if not self.is_empty() else None
        
    def peek(self) -> Optional[int]:
        """Повертає елемент на вершині без його видалення. None, якщо порожній."""
        return self._items[-1] if not self.is_empty() else None
        
    def size(self) -> int:
        """Повертає поточний розмір стека."""
        return len(self._items)
        
    def is_empty(self) -> bool:
        """Перевіряє, чи порожній стек."""
        return len(self._items) == 0

# Демонстрація незалежності даних
st1 = Stack()
st2 = Stack()
st1.push(42)
print(f"independence Stack: st1 size={st1.size()}, st2 size={st2.size()}")

# Тести
class TestStack(unittest.TestCase):
    def test_normal_operations(self):
        st = Stack()
        st.push(10)
        st.push(20)
        self.assertEqual(st.peek(), 20)
        self.assertEqual(st.pop(), 20)
        self.assertEqual(st.size(), 1)
        
    def test_boundary_empty(self):
        st = Stack()
        self.assertTrue(st.is_empty())
        self.assertIsNone(st.pop())
        self.assertIsNone(st.peek())
        
    def test_invalid_type(self):
        st = Stack()
        with self.assertRaises(TypeError):
            st.push("не число")
