from random import randrange


class Dinosaur(object):
    def __init__(self, size):
        self.size = size

    def roar(self):
        raise NotImplementedError


class TyrannosaurusRex(Dinosaur):
    def __init__(self, size):
        super().__init__(size)
        self.name = 'Tyrannosaurus Rex'

    def roar(self):
        return 'WROOOooooOOaaarrr!'


class Triceratops(Dinosaur):
    def __init__(self, size):
        super().__init__(size)
        self.name = 'Triceratops'

    def roar(self):
        return 'buff! buff!'


class JurassicPark(object):
    """Represents the Jurassic Park from the famous movie"""

    def __init__(self):
        """Creates a Jurassic Park"""
        self._tyrannosaurus = []
        self._triceratops = []

    def add_dinosaur(self, dino):
        if dino.__class__ == 'TyrannosaurusRex':
            self._tyrannosaurus.append(dino)
        elif dino.__class__ == 'Triceratops':
            self._triceratops.append(dino)

    def add_trex(self, trex):
        self._tyrannosaurus.append(trex)

    def add_triceratops(self, tri):
        self._triceratops.append(tri)

    def battle(self):
        for trex in self._tyrannosaurus:
            print('A {0} ({1}): {2}'.format(trex.name, trex.size, trex.roar()))
        for tri in self._triceratops:
            print('A {0} ({1}): {2}'.format(tri.name, tri.size, tri.roar()))

        num_trex = len(self._tyrannosaurus)
        num_tri = len(self._triceratops)

        if num_trex <= 0 or num_tri <= 0:
            print('No battle is possible. Peace.')
            return

        if num_trex > num_tri * 2.:
            print('Tyrannosaurus killed the triceratops herd')
            self._triceratops = []
        else:
            if sum([dinosaur.size for dinosaur in self._tyrannosaurus]) < sum(
                    [dinosaur.size for dinosaur in self._triceratops]):
                print('Triceratops killed one tyrannosaurus!')
                try:
                    del self._tyrannosaurus[-1]
                except IndexError:
                    pass
            else:
                print('Battle finishes OK')