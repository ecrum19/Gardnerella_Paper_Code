import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def excel_parse (location, column):
    df = pd.read_excel(location, sheet_name='Sheet1')  # reads xlsx
    output_list_x = df[column]      # assigns values of one column to list
    return output_list_x

def fix_matrix(location):
    with open(location, 'r') as f:
        data = f.readlines()

    # 67 genomes; 68 lines
    # data is in indices 1-67
    # your file is tab delimited

    matrix = np.zeros((67, 67))

    # fill in lower triangular matrix
    for i in range(67):
        line = data[i + 1]
        x = line.strip()
        x = x.split('\t')
        for j in range(len(x) - 1):
            matrix[i][j] = float(x[j + 1])

    # fill in horizontal; reflect across the horizontal
    for i in range(67):
        for j in range(67):
            if i == j:
                matrix[i][j] = 100.0
            else:
                if matrix[i][j] != 0 and matrix[j][i] == 0:
                    matrix[j][i] = matrix[i][j]

    np.savetxt('/Users/eliascrum/fastANI/Lacto_m.csv', matrix, delimiter=",", fmt= '%10.5f')
    return None


def make_plot(matrix):
    data = np.genfromtxt(matrix,delimiter=',')

    strains = excel_parse('/Users/eliascrum/Desktop/all_gasseri_paragasseri.xlsx', 'Strain')[0:67]
    print(strains)
    fig,ax = plt.subplots()
    im = ax.imshow(data,cmap='RdYlBu_r',vmin=90,vmax=100)

    ax.set_yticks(np.arange(len(strains)))
    ax.set_xticks(np.arange(len(strains)))

    ax.set_yticklabels(strains)
    ax.set_xticklabels(strains)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor",size=2)
    plt.setp(ax.get_yticklabels(),size=3)
    plt.colorbar(im)

    fig.tight_layout()

    fig.savefig('/Users/eliascrum/fastANI/heatmap.eps',format='eps')


make_plot('/Users/eliascrum/fastANI/Lacto_m.csv')