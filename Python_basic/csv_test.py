#!/usr/bin/env python3

import csv
import numpy as np

with open('../../data/hw1/test.csv') as fp:
    data = list(csv.reader(fp))
    # frist column is id
    data = np.array(data[1:])[:, 1:].astype(float)

print(data)
