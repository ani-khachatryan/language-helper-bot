import unittest
import translation


class TestTrans(unittest.TestCase):
    def test_en_ru(self):
        result = translation.translate("translation", 'ru')
        self.assertEqual(result, 'перевод')

    def test_random_default(self):
        result = translation.translate("綠色")
        self.assertEqual(result, "green")

if __name__ == '__main__':
    unittest.main()