import numpy as np
import Protein as p

class Beam2D:

    def __init__(self, beam_size=50):
        self.bs = beam_size

    def run_beam(self, protein, cur_score, coors):

        cur_coors, cur_scores = [coors], [cur_score]
        for i, amino in enumerate(protein[len(coors):], start=len(coors)):
            # print(i, amino)
            candi_coors, candi_scores = self.get_candidates(cur_coors, cur_scores, protein)
            cur_coors, cur_scores = candi_coors[:self.bs], candi_scores[:self.bs] 
            # cur_coors, cur_scores = candi_coors, candi_scores
        # print(cur_coors[0], cur_scores[0])
        return cur_coors, cur_scores


    def get_candidates(self, coors, scores, protein):

        candidates, candi_scores = [], []

        # print(proteins, scores)
        for i, parent in enumerate(coors):
            # print('parent', parent)
            children, c_scores = self.make_children(parent, scores[i], protein)
            candidates += children
            candi_scores += c_scores
        # print(candidates)
        score_sorted, candi_sorted = zip(*sorted(zip(candi_scores, candidates),reverse=True))
        # print(candi_sorted[0], score_sorted[0])
        # print(score)
        
        return candi_sorted, score_sorted
    

    def make_children(self, coors, old_score, protein):
        
        new_coors = [self.check_coor(coors, i) for i in range(4)]
        children = [coors + [coor] for coor in new_coors if coor]
        scores = [old_score + self.update_score(child, protein) for child in children]
        # print('make children', children, scores)
        # print(children[0], scores[0])
        return children, scores


    def update_score(self, coors, protein):

        score = 0
        for i, coor in enumerate(coors[:-3]):
            if abs(coor[0] - coors[-1][0]) + abs(coor[1] - coors[-1][1]) == 1 and protein[i] == 'H':
                score += 1
        # print(score)
        return score
    
    def check_coor(self, coors, direction):

        old_coor = coors[-1]
        directions = [(old_coor[0] - 1, old_coor[1]), (old_coor[0] + 1, old_coor[1]), 
                      (old_coor[0], old_coor[1] + 1), (old_coor[0], old_coor[1] - 1)]

        if directions[direction] not in coors:
            return directions[direction]
        return False


if __name__=='__main__':

    p_obj = p.Protein2D(protein)
    score = p_obj.get_score(p_obj.coors, protein)

    bm = Beam2D()
    coors, candi_coors = bm.run_beam(protein, score, p_obj.coors)



