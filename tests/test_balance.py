import unittest
import solarpv.balance


class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_for_valid_calc_annuity_factor(self):
        self.assertEqual(solarpv.balance.calc_annuity_factor(rate=0.0, years=10), 0.1)
