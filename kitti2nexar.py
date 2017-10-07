#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Martin Kersner, m.kersner@gmail.com
# 2017/10/07

import os
import argparse

import pandas as pd

def main():
    input_dir, output_file = parse_args()

    df = pd.DataFrame([], columns=["image_filename", "x0", "y0", "x1",
                                   "y1", "label", "confidence"])

    kitti_ann_files = os.listdir(input_dir)
    for ann_file in kitti_ann_files:
        df_tmp = pd.read_csv(os.path.join(input_dir, ann_file),
                delimiter=" ", header=None,
                names=["label", "truncated", "occluded", "alpha", "x0", "y0",
                       "x1", "y1", "height", "width", "length", "x",
                       "y", "z", "rotation_y", "confidence"])

        df_tmp["image_filename"] = ".".join(ann_file.split(".")[0:-1])
        df = pd.concat([df, df_tmp[["image_filename", "x0", "y0",
                                    "x1", "y1", "label", "confidence"]]])

    df['label'] = df['label'].apply(lambda label: label.lower())
    df.to_csv(output_file, index=False, header=True)

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', required=True, action='store',
            help='Directory with KITTI annotations')

    parser.add_argument('-o', required=True, action='store',
            help='Nexar CSV format for evaluation.')

    args = parser.parse_args()
    return args.i, args.o

if __name__ == "__main__":
    main()
