import numpy as np
from mpl_toolkits import mplot3d as plt3d
import matplotlib.pyplot as plt

class Protein:

    def __init__(self, protein, two_d=True):
        self.two_d = two_d
        self.protein = protein
        self.start_pos = len(self.protein) - 1
        self.coors = self.init_protein()
        


    def init_protein(self):
        if self.two_d:
            cur_coors = [(self.start_pos + i, self.start_pos) for i,_ in enumerate(self.protein)]
        else:
            cur_coors = [(self.start_pos + i, self.start_pos, self.start_pos) for i,_ in enumerate(self.protein)]
        return cur_coors
    
    def plot_protein(self, protein, coors):
        if self.two_d:
            x, y = zip(*coors)
            plt.scatter(x, y,zorder=2)
            plt.plot(x, y, color='black',zorder=1)
            plt.axis('off')
            plt.show()
        else:
            x, y, z = zip(*coors)
            fig = plt.figure()
            ax = fig.gca(projection='3d')
            ax.plot(x, y, z, 'k', zorder=1)
            ax.scatter(x, y, z, zorder=2)
            # ax.set_yticklabels([])
            # ax.set_xticklabels([])
            # ax.set_zticklabels([])
            plt.axis('off')
            plt.show()
    

if __name__ == '__main__':
    protein = 'HPPHHPPHHHPPHPHP'
    pr = Protein(protein, two_d=True)
    pr.plot_protein(pr.protein, pr.coors)
