import numpy as np
import csv
import matplotlib.pyplot as plt
import json
import math as m
import os
import pandas as pd
import scipy.interpolate as sp
data = os.listdir("/Users/bhagyasubrayan/Desktop/ZTF")
data.sort()
data.remove('.DS_Store')
f_txt = [i for i in data if i.endswith('.txt')]
for j in range(len(f_txt)):
    f_txt[j] = f_txt[j].replace(('.'+'_'),'')
f_g = [list(i) for j, i in groupby(f_txt, lambda a: a.split('.')[0])]
f_g.remove(f_g[-1])
def extract(filename):
    with open(filename) as file:
        file_line = file.readline()
        a = file_line.strip().split(' ',2)
        return a[2]
type_II= []
f_g
for j in range(0,len(f_g)):
    name = "/Users/bhagyasubrayan/Desktop/ZTF/"+ f_g[j][0]
    print(f_g[j][0])
    print(extract(name))
    if(extract(name) == 'II'):
        type_II.append(f_g[j])
    else:
        continue
len(type_II)
