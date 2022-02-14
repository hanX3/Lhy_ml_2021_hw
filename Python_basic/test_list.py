#!/usr/bin/env python3

import torch
import csv
import numpy as np

with open('../../data/hw1/test.csv') as fp:
    data = list(csv.reader(fp))
    # frist column is id, remove first column
    data = np.array(data[1:])[:, 1:].astype(float)
print(data)

feats = list(range(93))
data = data[:, feats]
# data = torch.FloatTensor(data)
print(data)

print(len(data))

indices = [i for i in range(len(data)) if i % 10 == 0]
data = torch.FloatTensor(data[indices])
# print(indices)
print(data)
print(data.shape)

print(data[:, 40:].shape)
print(data[:, 40:].mean(dim=0))
print(data[:, 40:].mean(dim=0).shape)
print(data[:, 40:].mean(dim=0, keepdim=True))
print(data[:, 40:].mean(dim=0, keepdim=True).shape)

print(data[:, 40:].std(dim=0))
print(data[:, 40:].std(dim=0).shape)
print(data[:, 40:].std(dim=0, keepdim=True))
print(data[:, 40:].std(dim=0, keepdim=True).shape)

data[:, 40:] = \
    (data[:, 40:] - data[:, 40:].mean(dim=0, keepdim=True)) \
    / data[:, 40:].std(dim=0, keepdim=True)
print(data)
print(data.shape[1])
