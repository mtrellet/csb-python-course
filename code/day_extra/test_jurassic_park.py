import unittest
from random import randrange


from .jurassic_park import Dinosaur, Triceratops, TyrannosaurusRex


class TestJurassicPark(unittest.TestCase):

    def test_new_dino(self):
        dino = Dinosaur(100)
        self.assertEqual(dino.size, 100)
        self.assertNotEqual(dino.size, 200)

    def test_new_triceratops(self):
        triceratops = Triceratops(randrange(5, 15))
        self.assertTrue(5 <= triceratops.size <= 15)
        self.assertEqual(triceratops.roar(), 'buff! buff!')

    # Your turn!!!
