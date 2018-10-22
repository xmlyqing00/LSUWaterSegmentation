import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cmp_estimations(csv0_path, csv1_path):
    
    est0_df = pd.read_csv(csv0_path)
    est1_df = pd.read_csv(csv1_path)

    plt.figure()
    est0_df['merged_ratio'].plot()
    plt.ylim(-0.3, 1.1)
    plt.figure()
    est1_df['merged_ratio_smoothed'].plot()
    plt.ylim(-0.3, 1.1)
    
    plt.show()


if __name__ == '__main__':

    root_folder = '/Ship01/Dataset/flood/canyu_result/Houston'
    csv0_path = os.path.join(root_folder, 'waterlevel_pier_original.csv')
    csv1_path = os.path.join(root_folder, 'waterlevel_pier_smoothed1.csv')

    cmp_estimations(csv0_path, csv1_path)