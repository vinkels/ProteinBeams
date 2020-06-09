import pandas as pd
import scipy as sc
import os
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.anova import AnovaRM


class Analyse():

    def __init__(self, result_dir):
        self.dir = result_dir
        
    def parse_results(self, results_dir):
        # all_dfs = []
        all_dfs = []
        all_dfs = [ ]
        for result in os.listdir(results_dir):
            params = result.split('_')
            temp_df = pd.read_csv(results_dir+result, names=['protein', 'coors', 'score'])
            temp_df['score'] = temp_df['score'].astype(int)
            temp_df['length'] = int(params[1])
            temp_df['beam_size'] = int(params[2].strip('bs'))
            all_dfs.append(temp_df)
        df = pd.concat(all_dfs)
        return df
    
    def plot_results(self, df):

        for length in df['length'].unique():
            cur_df = df[df['length'] == length]

            
            # print(df_max)
            plt.figure()
            sns.boxplot(y=cur_df['score'], x=cur_df['beam_size']).set_title(f'scores for different beam sizes for proteins of length {length}')
            plt.savefig(f'plots/l{length}_scores_beamsize.png')

        df_max = df[df['length'] == 100]
        # sns.set()
        # sns.pointplot(data=df_max, x='beam_size', y='score', hue='length', dodge=True,
	    #   capsize=.1, errwidth=1, palette='colorblind')
        # plt.show()
        # two_data.loc['cat']
        # j = sc.stats.ttest_rel(df_max[df_max['beam_size']==20]['score'], df_max[df_max['beam_size']==50]['score'])
        # # print(jup)

        # aovrm = AnovaRM(df_max, 'score', 'protein', within=['beam_size'])
        # print([sc.stats.shapiro(df_max[df_max['beam_size'] == size]['score']) for size in df_max['beam_size'].unique()])
        # res = aovrm.fit()
        # print(aovrm)
        # print(res)


    

if __name__ == '__main__':

    a = Analyse('results/')
    df = a.parse_results(a.dir)
    a.plot_results(df)

