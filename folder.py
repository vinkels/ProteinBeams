import numpy as np

class Protein:

    def __init__(self, protein):
        self.protein = protein
        self.cur_coors = []
        self.start_pos = len(self.protein) - 1

    def init_2d(self):
        self.cur_coors = [(self.start_pos + i, self.start_pos) for i,_ in enumerate(self.protein)]
        print(self.cur_coors)
        

    def init_3d(self):
        self.cur_coors = [(self.start_pos + i, self.start_pos, self.start_pos) for i,_ in enumerate(self.protein)]
        print(self.cur_coors)
    
    

if __name__ == '__main__':
    fold = Folder(20, 1000)
    prot_lst = gen.p_generator()
    gen.get_hp_dist(prot_lst)