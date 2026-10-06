import unittest

class LightSwitch:
    """Клас вимикача світла з лічильником кількості перемикань."""
    
    def __init__(self, on: bool = False):
        self._is_on = bool(on)
        self._switches_count = 0
        
    def toggle(self) -> None:
        """Змінює стан вимикача на протилежний та збільшує лічильник."""
        self._is_on = not self._is_on
        self._switches_count += 1
        
    def is_on(self) -> bool:
        """Повертає поточний стан вимикача."""
        return self._is_on
        
    def switches(self) -> int:
        """Повертає загальну кількість перемикань."""
        return self._switches_count

# Демонстрація незалежності даних
sw1 = LightSwitch()
sw2 = LightSwitch()
sw1.toggle()
print(f"independence LightSwitch: sw1 on? {sw1.is_on()}, sw2 on? {sw2.is_on()}")

# Тести
class TestLightSwitch(unittest.TestCase):
    def test_normal_toggle(self):
        sw = LightSwitch()
        sw.toggle()
        self.assertTrue(sw.is_on())
        self.assertEqual(sw.switches(), 1)
        
    def test_multiple_toggles(self):
        sw = LightSwitch(on=True)
        sw.toggle()  # -> off
        sw.toggle()  # -> on
        self.assertTrue(sw.is_on())
        self.assertEqual(sw.switches(), 2)
        
    def test_initial_state(self):
        sw = LightSwitch()
        self.assertFalse(sw.is_on())
        self.assertEqual(sw.switches(), 0)
