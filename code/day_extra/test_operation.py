import unittest


class TestOperation(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 3, 2]), 6, "Should be 6")

    def test_max(self):
        self.assertEqual(max([1, 3, 2]), 3, "Should be 3")

    def test_useless_operation(self):
        self.assertEqual(sum([1, 3, 2]) + max([1, 4, 2]), 9, "Should be 9")


if __name__ == "__main__":
    unittest.main()
