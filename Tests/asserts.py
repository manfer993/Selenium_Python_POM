import unittest


class Asserts(unittest.TestCase):

    def test_equal(self):
        a = 5
        b = 5
        self.assertEqual(a, b, 'this is an error 1')

    def test_almost_equal(self):
        a = 1.000001
        b = 1.000004
        self.assertAlmostEqual(a, b, 5, 'this is an error 2')

    def test_true(self):
        a = 5
        b = 5
        self.assertTrue(a == b, 'this is an error 3')

    def test_greater_equal(self):
        a = 5
        b = 2
        self.assertGreaterEqual(a, b, 'this is an error 4')

    def test_less_equal(self):
        a = 5
        b = 9
        self.assertLessEqual(a, b, 'this is an error 5')

    def test_list_equal(self):
        a = [5, 'first', True, [1, 2, 3]]
        b = [5, 'first', True, [1, 2, 3]]
        self.assertListEqual(a, b, 'this is an error 6')

    def test_tuple_equal(self):
        a = (5, 'red', 'Ford')
        b = (5, 'red', 'Ford')
        self.assertTupleEqual(a, b, 'this is an error 7')

    def test_dict_equal(self):
        a = {'id': 1, 'name': 'manuel', 'lastName': 'Munoz'}
        b = {'id': 1, 'name': 'manuel', 'lastName': 'Munoz'}
        self.assertDictEqual(a, b, 'this is an error 8')


if __name__ == '__main__':
    unittest.main()
