import os
import Protein as p
import Beam as b
import csv

def main():
    protein_folder = 'proteins/final/'
    protein_dict = {}
    beam_range = [160, 170, 180, 190, 200]
    for beam_size in beam_range:
        # for hp in os.listdir('proteins/final/'):
        hp = 'HP_100'
        finals = []
        protein_length = int(hp.split('_')[1])
        for protein in open(protein_folder+hp, 'r'):


            p_obj = p.Protein2D(protein)
            score = p_obj.get_score(p_obj.coors, protein)

            bm = b.Beam2D(beam_size=beam_size)
            coors, scores = bm.run_beam(protein, score, p_obj.coors)
            finals.append([protein, coors[0], scores[0]])
        print(beam_size, finals[-1][-1])
        
        with open(f'results/{hp}_bs{bm.bs}_beamResults.csv', 'w') as f:
            writer = csv.writer(f)
            for result in finals:
                writer.writerow(result)
        
            

main()
