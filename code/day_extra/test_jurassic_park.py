import unittest
from random import randrange


from .jurassic_park import Dinosaur, Triceratops, TyrannosaurusRex, JurassicPark


class TestJurassicPark(unittest.TestCase):

    def test_new_dino(self):
        dino = Dinosaur(100)
        self.assertEqual(dino.size, 100)
        self.assertNotEqual(dino.size, 200)

    def test_new_triceratops(self):
        triceratops = Triceratops(randrange(7, 10))
        self.assertTrue(5 <= triceratops.size <= 15)
        self.assertEqual(triceratops.roar(), 'buff! buff!')

    def test_new_trex(self):
        trex = TyrannosaurusRex(randrange(5, 15))
        self.assertTrue(5 <= trex.size <= 15)
        self.assertEqual(trex.roar(), 'buff! buff!')

    def test_park(self):
        park = JurassicPark()
        self.assertEqual(park._tyrannosaurus, [])
        self.assertEqual(park._triceratops, [])

        trex = TyrannosaurusRex(randrange(5, 15))
        triceratops = Triceratops(randrange(7, 10))

        park.add_trex(trex)

        self.assertEqual(len(park._tyrannosaurus), 1)
        self.assertEqual(len(park._triceratops), 0)

        park.add_triceratops(triceratops)

        self.assertEqual(len(park._tyrannosaurus), 1)
        self.assertEqual(len(park._triceratops), 1)

        park.battle()

        self.assertEqual(len(park._tyrannosaurus), 0)


if __name__ == "__main__":
    unittest.main()
