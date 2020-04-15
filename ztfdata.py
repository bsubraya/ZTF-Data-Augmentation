import numpy as np
import csv
import matplotlib.pyplot as plt
import json
import math as m
import os
import pandas as pd
import scipy.interpolate as sp
from itertools import groupby
from scipy import interpolate
from collections import OrderedDict
from varname import varname
train_data = os.listdir("/Users/bhagyasubrayan/Desktop/ZTF")
print(train_data)
train_data.sort()
train_data.remove('.DS_Store')
for j in range(len(train_data)):
    train_data[j] = train_data[j].replace(('.'+'_'),'')
train_data.remove(train_data[-1])
train_data.remove(train_data[-1])
len(train_data)
#train_data.remove(train_data[-1])
#train_data.remove(train_data[-2])
#train_data[-2]
#Ordering them like pairing the files with g,r files together
f_g = [list(i) for j, i in groupby(train_data, lambda a: a.split('.')[0])]
def parse_my_file(filename):
    with open(filename) as f:
        lines = f.readlines()[1:]
        for line in lines:
            yield line.strip().split(' ', 3)
        f.close()
def extract(filename):
    with open(filename) as file:
        file_line = file.readline()
        a = file_line.strip().split(' ',2)
        return a[2]
f_g[-1]
#Routine which plots the data in the files back tot back for g and r files from the data
#Pulling each files from a band at a time; converting to dataframe and plotting required columns
g_group = []
r_group = []
no_data = []
for i in range(0,len(f_g)):
    for j in range(0,2):
        #print(f_g[i][j])
        f_name = "/Users/bhagyasubrayan/Desktop/ZTF/"+ f_g[i][j]
        df_j = pd.DataFrame(parse_my_file(f_name),columns = ['mjd','filter','flux','flux_err'])
        df_j = df_j.sort_values(by = ['mjd']).reset_index(drop = 'True')
        df_j = df_j.apply(pd.to_numeric)
        #divide_to_group(f_name)
        #print(len(df_j))
        if(len(df_j) == 0):
            no_data.append(f_g[i][j])
            print('Encountered a no_data file', f_g[i][j])
            continue
        #print(df_j.iloc[0]['filter'])
        #print(no_data)
        #plt.title('LC_'+f_g[i][j])
        #plt.plot(df_j['mjd'],df_j['flux'],'o')
        #plt.errorbar(df_j['mjd'],df_j['flux'],yerr = df_j['flux_err'],fmt='o')
        if (df_j.iloc[0]['filter'] == 1):
            g_group.append(f_g[i][j])
        else:
            r_group.append(f_g[i][j])
    #plt.gca().invert_yaxis()
    #plt.show()
#Classify different light curves from the g and r group.First starting with g group:
def divide_to_group(list):
    group_df = pd.DataFrame()
    d = []
    type = []
    mega_data=[]
    for k in range(0,len(list)):
        name = "/Users/bhagyasubrayan/Desktop/ZTF/"+list[k]
        type.append(extract(name))
    #print(type)
    #print(name)
    #print(extract(name))
    group_df['Type'] = type
    a1 = group_df.groupby('Type').size()
    print(a1)
    a2= name.split('.')
    #print(a2[1])
    for j in range(0,len(a1)):
        cat_j = pd.DataFrame()
        c_j = []
        d.append(a1.index[j])
        s = str(a1.index[j])
        #print(d)
        #print(s)
        for k in range(0,len(list)):
            name = "/Users/bhagyasubrayan/Desktop/ZTF/"+list[k]
            if(extract(name) == d[j]):
                c_j.append(list[k])
        cat_j['Type'+s+'_'+a2[1]] = c_j
        #mega_data.append(cat_j)
        #return mega_data[j]
divide_to_group(g_group)
divide_to_group(r_group)
print('Total g light curves:',len(g_group))
print('Total r light curves:',len(r_group))
print('Total no_data light curves:',len(no_data))
#Classify different light curves from the g and r group.First starting with g group
#plotting Type II supernovae in g band
#for g in range(0,10):
#    df_g = pd.DataFrame(parse_my_file("/Users/bhagyasubrayan/Desktop/ZTF/"+ type_II_g[g]),columns = ['mjd','filter','flux','flux_err'])
#    df_g = df_g.sort_values(by = ['mjd']).reset_index(drop = 'True')
#    df_g = df_g.apply(pd.to_numeric)
#    plt.title('LC_'+type_II_g[g])
#    plt.plot(df_g['mjd'],df_g['flux'],'o')
#    plt.errorbar(df_g['mjd'],df_g['flux'],yerr = df_g['flux_err'],fmt='o')
#    plt.gca().invert_yaxis()
#    plt.show()
print(g_group)
