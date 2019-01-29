# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:53:50 2018

@author: abhi
"""
import kmeans_Knn as kk
import randomized_multiple_kdtreed as rmk
import common_function as cf
import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
import pickle


def multi_kdtree(data,y,test_data,test_y,no_of_trees = 5,no_of_dimensions = 600,variance = False,comparisions = 4) :
    a = time.time()
    multi_trees = rmk.randomized_trees(np.array(data),label = y,no_of_trees = no_of_trees,no_of_dimensions = no_of_dimensions,variance = variance,comparisions = comparisions )
    multi_trees.make_data_sets()
    multi_trees.make_tree()
    accuracy = []
    b = time.time()
    tree_building_time = b-a
    a = time.time()
    
    #print(test_y)
    for temp_x,temp_y in zip(test_data,test_y) :
        #print(temp_x)
        lst = [val[1] for val in multi_trees.get_nearest(temp_x)]
        #print(lst)
        if temp_y == max(set(lst), key=lst.count) :
            accuracy.append(1)
        else :
            accuracy.append(0)
       
            
    b = time.time()
    prediction_time = b-a
    
    return (sum(accuracy)/len(test_data))*100,tree_building_time,prediction_time  

def kmeans_tree(data,y,test_data,test_y,k = 3,no_of_comparisions = 100,clustring_iteration = 7):
    a =time.time() 
    loc_kk = kk.nary_tree(points,y,k,no_of_comparisions,clustring_iteration)
    loc_kk.make_tree()
    accuracy = []
    b = time.time()
    tree_building_time = b-a
    a = time.time()
    
    for temp_x,temp_y in zip(test_data,test_y) :
        
        if temp_y == loc_kk.get_nearest(temp_x)[0][1][1]:
            accuracy.append(1)
        else :
            accuracy.append(0)
    b = time.time()
    prediction_time = b-a
    
    return (sum(accuracy)/len(test_data))*100,tree_building_time,prediction_time  

def single_kdtree(data,y,test_data,test_y,cols,compare) :
    a = time.time() 
    loc_rmk = rmk.knn_kdtree(data,y,cols,compare)
    loc_rmk.make_tree()
    accuracy = []
    b = time.time() 
    tree_building_time = b-a
    a = time.time() 
    for temp_x,temp_y in zip(test_data,test_y) :
        if temp_y == loc_rmk.get_nearest(temp_x)[0][1]:
            accuracy.append(1)
        else :
            accuracy.append(0)
 
    b = time.time() 
    prediction_time = b-a
    return (sum(accuracy)/len(test_data))*100,tree_building_time,prediction_time  

if __name__ == "__main__" :
    