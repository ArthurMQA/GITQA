import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)

    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)

    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)

    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_exp(self):
        "Возведение в степень"
        self.assertEqual(calc_me(7, 2,"^"), 49)

    def test_unkn_oper(self):
        """Негативный, ввод неизвестной операции"""
        self.assertEqual(calc_me(7, 2,"!"), 'Unknown operation')

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')

    def test_num1_none(self):
        """Негативный, отсутствие x"""
        self.assertEqual(calc_me(None, 2,"/"), 'ERROR: send me Number1')

    def test_num2_none(self):
        """Негативный, отсутствие y"""
        self.assertEqual(calc_me(4, None,"/"), 'ERROR: send me Number2')

    def test_num1_simb(self):
        """Негативный, ввод символьных значений  Number1"""
        self.assertEqual(calc_me(".1", 3,"+"), 'ERROR: now it is does not supported')

    def test_num2_simb(self):
        """Негативный, ввод символьных значений Number2"""
        self.assertEqual(calc_me(4, "!","/"), 'ERROR: now it is does not supported')





if __name__ == '__main__':
    unittest.main(verbosity=2) 