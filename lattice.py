import numpy as np

class Lattice:
    def __init__(self, vectors, rotation_angles, kind):
        self.vectors = vectors.tolist()
        self.rotation_angles = rotation_angles
        self.kind = kind


class FCC3DLattice(Lattice):
    def __init__(self):
        Lattice.__init__(self, np.array([[1,1,0],
                                         [1,-1,0],
                                         [-1,1,0],
                                         [-1,-1,0],
                                         [0,1,1],
                                         [0,-1,1],
                                         [1,0,1],
                                         [-1,0,1],
                                         [0, 1, -1],
                                         [0, -1, -1],
                                         [1, 0, -1],
                                         [-1, 0, -1]
                                         ]),
                         [0, np.pi / 2, -np.pi / 2, np.pi],
                         "3D_FCC")


class CubicLattice(Lattice):
    def __init__(self):
        Lattice.__init__(self, np.array([[1,0,0],
                                         [0,1,0],
                                         [0,0,1],
                                         [-1,0,0],
                                         [0,-1,0],
                                         [0,0,-1],
                                         ]),
                             [],
                             "cubic")


class KWLattice(Lattice):
    def __init__(self):
        Lattice.__init__(self, np.array([[0,1,2],
                                         [0,1,-2],
                                         [0,-1,2],
                                         [0,-1,-2],
                                         [0,2,1],
                                         [0,2,-1],
                                         [0,-2,1],
                                         [0,-2,-1],
                                         [1,0,2],
                                         [1,0,-2],
                                         [-1,0,2],
                                         [-1,0,-2],
                                         [2,0,1],
                                         [2,0,-1],
                                         [-2,0,1],
                                         [-2,0,-1],
                                         [2,1,0],
                                         [-2,1,0],
                                         [2,-1,0],
                                         [-2,-1,0],
                                         [1,2,0],
                                         [-1,2,0],
                                         [1,-2,0],
                                         [-1,-2,0],
                                         ]),
                         [],
                         "knight's walk")


class DiamondLattice(Lattice):
    def __init__(self):
        Lattice.__init__(self, np.array([[1,1,1],
                                         [-1,-1,1],
                                         [1,-1,-1],
                                         [-1,1,-1],
                                         [-1,-1,-1],
                                         [1,1,-1],
                                         [-1,1,1],
                                         [1,-1,1],
                                         ]),
                         [],
                         "diamond")
