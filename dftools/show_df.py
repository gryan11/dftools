import argparse, sys
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file')
    args = parser.parse_args(argv)
    df = pd.read_csv(args.csv_file, index_col=0)
    print(df)


