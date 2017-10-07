#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Martin Kersner, m.kersner@gmail.com
# 2017/10/07

import argparse

import pandas as pd

def main():
    input_file, output_file = parse_args()

    df = pd.read_csv(input_file, delimiter=" ", header=None,
            names=["frame", "xmin", "ymin", "xmax",
                   "ymax", "occluded", "label"])

    df['confidence'] = 1.0

    df.to_csv(output_file,
            index=False,
            columns=["frame", "xmin", "ymin", "xmax",
                     "ymax", "label", "confidence"],
            header=["image_filename", "x0", "y0", "x1",
                    "y1", "label", "confidence"])

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', required=True, action='store',
            help='Udacity CSV ground file downloaded from challenge website.')

    parser.add_argument('-o', required=True, action='store',
            help='Nexar CSV ground truth format for evaluation.')

    args = parser.parse_args()
    return args.i, args.o

if __name__ == "__main__":
    main()
