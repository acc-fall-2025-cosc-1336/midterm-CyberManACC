# tests/question_tests.py
# write function tests here, don't add input('') statements here!
import unittest
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))


from src.question_a.question_a import use_global
import src.question_a.question_a as qa
from src.question_b.question_b import is_prime
from src.question_c.question_c import get_assessment_value, get_tax_assessed
from src.question_d.question_d import get_person_category


class Test_Config(unittest.TestCase):
    def test_config(self):
        self.assertTrue(True)



class Test_QuestionA(unittest.TestCase):
    def setUp(self):
        # ensure no cross-test bleed for the global
        qa.GLOBAL_VALUE = 0

    def test_use_global_modifies_global(self):
        qa.GLOBAL_VALUE = 41
        result = use_global()
        self.assertEqual(42, result)
        self.assertEqual(42, qa.GLOBAL_VALUE)

    def test_use_global_again(self):
        qa.GLOBAL_VALUE = 0
        self.assertEqual(1, use_global())
        self.assertEqual(2, use_global())
        self.assertEqual(2, qa.GLOBAL_VALUE)



class Test_QuestionB(unittest.TestCase):
    def test_is_prime_examples(self):
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(11))







class Test_QuestionC(unittest.TestCase):
    def test_get_assessment_value_examples(self):
        self.assertEqual(get_assessment_value(10000), 6000)
        self.assertEqual(get_assessment_value(20000), 12000)

    def test_get_tax_assessed_examples(self):
        self.assertEqual(get_tax_assessed(6000), 43.20)
        self.assertEqual(get_tax_assessed(10000), 72)



class Test_QuestionD(unittest.TestCase):
    def test_get_person_category_examples(self):
        self.assertEqual(get_person_category(1), "infant")
        self.assertEqual(get_person_category(2), "child")
        self.assertEqual(get_person_category(14), "teenager")
        self.assertEqual(get_person_category(20), "adult")

    def test_get_person_category_invalid(self):
        self.assertEqual(get_person_category(-1), "Invalid number")
        self.assertEqual(get_person_category(126), "Invalid number")


if __name__ == "__main__":
    unittest.main()
