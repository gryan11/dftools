"""
minigzip&0.49&0.78&0.60&0.83&0.64&{\bf 0.72}\\
djpeg&0.49&0.64&0.55&0.82&0.52&{\bf 0.64}\\
mutool&1.0&0.01&\textbf{0.02}&1.0&0.01& \textbf{0.02}\\
xmllint & 0.97 & 0.39 & \textbf{0.56}  & 0.97 & 0.39 & \textbf{0.56}\\
readelf&0.17&0.95&0.30&0.18&0.93 & {\bf 0.31} \\
objdump&0.68&0.77&0.72&0.90&0.75& {\bf 0.82}\\
strip&0.53&0.81&0.64&0.86&0.77& {\bf 0.82} \\
"""

import pandas as pd
import numpy as np
import sys, argparse
from numbers import Number


def df_to_latex(df, digits=2, pcols=None):
    table = "\\begin{tabular}{l "
    if pcols:
        for _ in range(len(df.columns)):
            table += "p{"+str(pcols)+"cm} "
    else:
        table += "r"*len(df.columns)
    table +="}\n"
    table += "\\toprule\n"
    table += '&'+'&'.join(map(lambda x: x.replace('_', '\\_'), list(df.columns))) + '\\\\' + '\n'
    table += "\\midrule\n"

    df = np.round(df, digits)

    for i, r in df.iterrows():
        table += str(i) + '&'
        table += '&'.join(map(lambda x: str(x).replace('_','\\_') if isinstance(x, str) or isinstance(x, Number) and not np.isnan(x) else '-', list(r)))
        table += '\\\\'+'\n'

    table += '\\bottomrule\n'
    table += '\\end{tabular}\n'

    return table


def main(argv=sys.argv[1:]):

    parser = argparse.ArgumentParser()
    parser.add_argument('input_csv')
    parser.add_argument('-d', dest='digits', type=int, default=2)
    parser.add_argument('-pcols', dest='pcols', type=float)
    args = parser.parse_args(argv)

    df = pd.read_csv(args.input_csv, index_col=0)
    table = df_to_latex(df, args.digits, args.pcols)

    print(table)


if __name__ == '__main__':
    main()


