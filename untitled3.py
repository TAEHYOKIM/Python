#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:53:08 2018

@author: hbk
"""

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


import pickle
list = ['a', 'b', 'c']
with open('list.txt', 'wb') as f:
    pickle.dump(list, f)
    
with open('list.txt', 'rb') as f:
    data = pickle.load(f) # 단 한줄씩 읽어옴
data


meta_file = "/Users/hbk/cifar-10-batches-py/batches.meta"
meta = unpickle(meta_file)
meta
len(meta[b'label_names'])
batch1_file = "/Users/hbk/Downloads/cifar-10-batches-py/data_batch_1"
batch1 = unpickle(batch1_file)
batch1.keys()
