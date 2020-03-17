import numpy as np
import random as rd
import matplotlib.pyplot as plt
import scipy.stats as stat

class Generator:

    def __init__(self, protein_length, n, unique=True):
        self.protein_length = protein_length
        self.n = n
        self.h_frac = 0.5
        self.unique = unique

    def p_generator(self):

        proteins = [tuple(np.random.randint(2, size=self.protein_length)) for i in range(self.n)]
        if not self.unique: 
            return proteins
        elif self.n > 2**self.protein_length:
            print('not enough combos')
            return proteins
        else:
            proteins = set(proteins)

        while len(proteins) < self.n:
            proteins = set([tuple(np.random.randint(2, size=self.protein_length)) for i in range(self.n * 20)])
        
        proteins = rd.sample(proteins, self.n)

        return proteins
    
    def get_hp_dist(self, proteins, plot=False):
        h_count = [protein.count(1) for protein in proteins]
        shap_wilk = stat.shapiro(h_count)
        
        if plot:
            plt.hist(h_count)
            plt.show()
        

        
if __name__ == '__main__':
    gen = Generator(20, 1000)
    prot_lst = gen.p_generator()
    gen.get_hp_dist(prot_lst)
