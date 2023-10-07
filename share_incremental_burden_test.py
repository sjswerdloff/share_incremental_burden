import unittest
from share_incremental_burden import redistribute_integer_dose_single_shot_by_weight, redistribute_integer_dose, redistribute_dose

class TestCase(unittest.TestCase):
    def test_redistribute_integer_dose_single_shot_by_weight(self):
        pass

    def test_redistribute_integer_dose(self):
        pass

    def test_redistribute_dose(self):
        result = redistribute_dose({'A':100, 'B': 100, 'C': 100}, 1)
        print(result)
        self.assertDictEqual(result,{'A':101, 'B': 100, 'C': 100})

        result = redistribute_dose({'A':99, 'B': 100, 'C': 100}, 1)
        print(result)
        self.assertDictEqual(result,{'A':99, 'B': 101, 'C': 100})
    
        result = redistribute_dose({'A':100, 'B': 200, 'C': 200}, 5)
        print(result)
        self.assertDictEqual(result,{'A':101, 'B': 202, 'C': 202})

        result = redistribute_dose({'A':100, 'B': 200, 'C': 200}, 3)
        print(result)
        self.assertDictEqual(result,{'A':101, 'B': 201, 'C': 201})

        result = redistribute_dose({'A':100, 'B': 200, 'C': 200}, 1)
        print(result)
        self.assertDictEqual(result,{'A':100, 'B': 201, 'C': 200})


        result = redistribute_dose({'A':100, 'B': 100, 'C': 100}, -1)
        print(result)
        self.assertDictEqual(result,{'A':99, 'B': 100, 'C': 100})

        result = redistribute_dose({'A':99, 'B': 100, 'C': 100}, -1)
        print(result)
        self.assertDictEqual(result,{'A':99, 'B': 99, 'C': 100})

        result = redistribute_dose({'A':100, 'B': 200, 'C': 200}, -1)
        print(result)
        self.assertDictEqual(result,{'A':100, 'B': 199, 'C': 200})

        result = redistribute_dose({'A':100, 'B': 200, 'C': 200}, -3)
        print(result)
        self.assertDictEqual(result,{'A':99, 'B': 199, 'C': 199})

        result = redistribute_dose({'A':100, 'B': 200, 'C': 200}, -5)
        print(result)
        self.assertDictEqual(result,{'A':99, 'B': 198, 'C': 198})

if __name__ == '__main__':
    unittest.main()