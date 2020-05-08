import argparse, sys
import pandas as pd

def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file')
    args = parser.parse_args(argv)
    df = pd.read_csv(args.csv_file)
    print(df)


