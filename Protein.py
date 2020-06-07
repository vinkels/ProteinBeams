import numpy as np
from mpl_toolkits import mplot3d as plt3d
import matplotlib.pyplot as plt

class Protein2D:

    def __init__(self, protein):
        self.protein = protein
        self.start_pos = len(self.protein) - 1
        self.coors = self.init_protein()

    def init_protein(self):

        cur_coors = [(self.start_pos, self.start_pos), (self.start_pos + 1, self.start_pos)]

        return cur_coors

    def place_protein(self, protein):
        coords = []
        for i, amino in enumerate(protein):
            coords.append((self.start_pos, self.start_pos + i))
        return coords
    
    def plot_protein(self, protein, coors):
        # if self.two_d:
        x, y = zip(*coors)
        plt.scatter(x, y,zorder=2)
        plt.plot(x, y, color='black',zorder=1)
        plt.axis('off')
        plt.show()

    def get_score(self, coors, protein):
        
        score = 0
        for i, coor in enumerate(coors[:-3]):
            for j, c in enumerate(coors[(i+3):]):
                if abs(coor[0] - c[0]) + abs(coor[1] - c[1]) == 1 and protein[j] == 'H':
                    score += 1
        return score

if __name__ == '__main__':
    # coors = [1,2,1,1,1,1,1]
    protein = 'HPPHPHHPPHHPPHHHHPH'
    pr = Protein2D(protein)
    coords = pr.place_protein(protein)
    # print(coords)
    scores = pr.get_score(coords, protein)
    print(scores)

    # new_prot = pr.get_coors(coors)
    # pr.plot_protein(pr.protein, new_coors)

    # [(1,0), (2,0), (3,0)]
