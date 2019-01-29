# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:54:33 2018

@author: abhi
"""
import numpy as np
import random
import math
import heapq
import time

# generates random coordinates as data for testing purpose
def random_coordinates(extremes,n,dimension) :   
    np.random.seed(2018);
    arr = []
    for i in range(n) :
        arr.append([])
        for j in range(dimension) :
            arr[i].append(random.randint(extremes[0],extremes[1]))
        #for extreme in extremes :
        #    arr[i].append(random.randint(extreme[0],extreme[1]))
    return arr

def EuclideanDistance(x,y):
        S = 0; #The sum of the squared differences of the elements
        for i in range(len(x)):
            S += math.pow(x[i]-y[i],2);
    
        return math.sqrt(S);

# normal formal Knn algorithm where each point chaeked with every other point iteratively
def normal_knn(data_set,y,test_data,test_y) :
    
    acc = 0
    a = time.time()
    for val,y_val in zip(test_data,test_y) :
        arr = []
        for data,temp_y in zip(data_set,y) :
            heapq.heappush(arr,(EuclideanDistance(data,val),temp_y))
        if y_val == heapq.heappop(arr)[1] :
            acc += 1
        
    b = time.time()
    return (acc/len(test_y))*100,b-a
    
    
