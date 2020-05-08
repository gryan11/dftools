import argparse, sys
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('csv1')
    parser.add_argument('csv2')
    args = parser.parse_args(argv)
    df1 = pd.read_csv(args.csv1, index_col=0)
    df1.columns = list(map(lambda x: '1-'+x, df1.columns))
    df2 = pd.read_csv(args.csv2, index_col=0)
    df2.columns = list(map(lambda x: '2-'+x, df2.columns))
    df = df1.join(df2)
    print(df)


