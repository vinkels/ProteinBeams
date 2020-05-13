import numpy as np
import Protein as p

class Beam2D:

    def __init__(self, protein_obj, sym_filt=True, beam_size=4):
        self.sym_filt=sym_filt
        self.p  = protein_obj
        self.bs = beam_size


    def make_children(self, protein_coors, old_score):
        
        new_coors = [self.p.check_coor(protein_coors, i) for i in range(4)]
        children = [protein_coors + [coor] for coor in new_coors if coor]
        scores = [old_score + self.p.update_score(child, self.p.protein) for child in children]
        return children, scores

    def get_candidates(self, proteins, scores):
        candidates = []
        candi_scores = []
        # print(proteins, scores)
        for i, protein in enumerate(proteins):
            children, c_scores = self.make_children(protein,scores[i])
            candidates += children
            candi_scores += c_scores

        score_sorted, candi_sorted = zip(*sorted(zip(candi_scores, candidates)))
        if self.bs > len(candi_scores):
            return candi_scores, candidates
        else:
            return candi_scores[:self.bm], candidates[:self.bm] 

        

if __name__=='__main__':
    prot = 'HPPHPPHHPH'

    proteins = [[(1,0), (2,0), (2, 1)]]
    protein = p.Protein2D(prot)
    start_coors = protein.coors[:2]
    # protein.plot_protein(prot, protein.coors)
    bm = Beam2D(protein)
    sc = [0]
    bm.get_candidates(proteins, sc)
    # bm.append_amino()
    # print(bm.directions)
    scores, candidates = [1, 6,5,2,1,5,7], [1, 0,1,0,1,0,1]
    # print(*zip(*sorted(zip(scores, candidates))))


