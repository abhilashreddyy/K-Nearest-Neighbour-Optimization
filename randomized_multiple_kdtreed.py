# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:07:36 2018

@author: abhi
"""



import heapq
import common_function as cf
import numpy as np
import random

points = []
nearest = []
class node(object) :
        def __init__(self,coords,lable):
            self.id = id
            self.point = coords
            self.left = None
            self.right = None
            self.lable = lable

#This represents our node.  Each node has a coordinate and a left and right node
class knn_kdtree(object):
    def __init__(self,temp_points,y,k,compare) :
        #print("hi")
        self.k = k
        self.points = temp_points#cf.random_coordinates([[1,100],[1,100]],300,k)
        self.y = y
        self.root = None
        self.final_pq = []
        self.traverse_pq = []
        self.comparisions = compare

        #print(self.points)







    def make_tree(self):

        for point,lable in zip(self.points,self.y) :
            self.root = self.insert(self.root,point,lable,0)

    # returns a priority queue with nearest neighbours
    def get_nearest(self,point) :
        self.compared = 0
        self.final_pq = []
        self.traverse_pq = []
        self.find_nearest(self.root,list(point),0)

        #print(self.final_pq)
        return self.final_pq





    # I have done so many experiments with finding nearest neighbour unfortunately notthing worked out
    '''def find_nearest(root, target, tree_depth,final_pq,k):
        axis = tree_depth % k
        next_node = None
        if root.left == None and root.right == None :
            heapq.heappush(final_pq,(EuclideanDistance(root.point,target),root.point))
        if target[axis] >= root.point[axis] :
            #if root.right == None :
            #    heapq.heappush(final_pq,(EuclideanDistance(root.point,target),root.point))
            if root.right != None :
                final_pq = find_nearest(root.right,target,tree_depth+1,final_pq,k)
            heapq.heappush(final_pq,(EuclideanDistance(root.point,target),root.point))
            next_node = root.left
        if target[axis] < root.point[axis] :
            #if root.left == None :
            #    heapq.heappush(final_pq,(EuclideanDistance(root.point,target),root.point))
            if root.left != None :
                final_pq = find_nearest(root.left,target,tree_depth+1,final_pq,k)
            heapq.heappush(final_pq,(EuclideanDistance(root.point,target),root.point))
            next_node = root.right
        if next_node != None:
            final_pq = find_nearest(next_node,target,tree_depth+1,final_pq,k)

        return final_pq'''


    # this function searches nearest neighbour
    def find_nearest(self,root, target, tree_depth):
        if self.comparisions > self.compared :

            axis = tree_depth % self.k
            if root == None :
                return
            if target[axis] >= root.point[axis] :
                self.find_nearest(root.right,target,tree_depth+1)
            elif target[axis] < root.point[axis] :
                self.find_nearest(root.left,target,tree_depth+1)
            #print(root.point,target)
            #print((root.point,root.lable))
            heapq.heappush(self.final_pq,(cf.EuclideanDistance(root.point,target),root.lable))
            self.compared += 1

    '''def find_nearest(root, target, tree_depth,final_pq,k):
        axis = tree_depth % k
        if root == None :
            return final_pq
        if target[axis] >= root.point[axis] :
            if root.right != None :
                final_pq = find_nearest(root.right,target,tree_depth+1,final_pq,k)
            if root.left != None and EuclideanDistance(target,root.left.point) < final_pq[0][0] :
                final_pq = find_nearest(root.left,target,tree_depth+1,final_pq,k)
        elif target[axis] < root.point[axis] :
            if root.left != None :
                final_pq = find_nearest(root.left,target,tree_depth+1,final_pq,k)
            if root.right != None and EuclideanDistance(target,root.right.point) < final_pq[0][0] :
                final_pq = find_nearest(root.right,target,tree_depth+1,final_pq,k)
        heapq.heappush(final_pq,(EuclideanDistance(root.point,target),root.point))
        return final_pq  '''






    #Generate our KDTree.  Depth starts at 0 and gets incremented as we recurse
    def insert(self,root,point,lable, tree_depth):
        axis = tree_depth % self.k
        if root == None :
            return node(point,lable)


        else :
            if root.point[axis] > point[axis] :
                root.left = self.insert(root.left,point,lable,tree_depth+1)
            elif root.point[axis]  <= point[axis] :
                root.right = self.insert(root.right,point,lable,tree_depth+1)

        return root

class randomized_trees() :
    def __init__(self,data,label = None,no_of_trees = 1,no_of_dimensions = 1,variance = True,include_projection = False,comparisions = 1) :
        self.comparisions = comparisions
        self.data = data
        self.no_of_trees = no_of_trees
        self.no_of_dimensions = no_of_dimensions
        self.variance = None
        self.variance_truth_value = variance
        self.include_projection = False
        self.trees = []
        self.lable = label

    def make_data_sets(self) :
        self.data = np.array(self.data)
        #print("variance : ",self.variance)




        self.trees_data = []

        if self.variance_truth_value :
            sorted_index = []
            self.variance = np.var(self.data,axis = 0)
            temp_sorted_index = np.argsort(self.variance)
            print("temp_sorted_index : ",temp_sorted_index)
            for val in reversed(temp_sorted_index) :
                sorted_index.append(val)
            print("variance : ",self.variance)
            print("data : ",self.data)

            for i in range(self.no_of_trees) :
                sorted_index = []
                for val in reversed(temp_sorted_index) :
                    sorted_index.append(val)
                print("sorted index : ",sorted_index)
                print("no_of_dimentions : " ,self.no_of_dimensions)
                b = sorted_index[:self.no_of_dimensions]
                print("b : ",b)
                random.shuffle(b)
                sorted_index[:self.no_of_dimensions] = b
                #b = sorted_index[self.no_of_dimensions:]
                #random.shuffle(b)
                #sorted_index[self.no_of_dimensions:] = b
                print("sorted index : ",sorted_index)
                temp_tree_data = self.data[:,sorted_index]
                print("temp_tree data : ",temp_tree_data)
                self.trees_data.append((temp_tree_data,sorted_index))
        else :
            tot_data = np.c_[self.data,self.lable]
            for i in range(self.no_of_trees) :
                np.random.shuffle(tot_data)
                self.trees_data.append((tot_data[:,:-1],tot_data[:,-1]))


    def make_tree(self) :
        #print(len(self.trees_data))
        for i,tree_data in enumerate(self.trees_data) :
            if self.variance_truth_value == True :
                self.trees.append(knn_kdtree(tree_data[0],self.lable,self.no_of_dimensions,self.comparisions))
            else :
                self.trees.append(knn_kdtree(tree_data[0],tree_data[1],self.no_of_dimensions,self.comparisions))
            self.trees[i].make_tree()

    def get_nearest(self,point) :
        point = np.array(point)
        nearest_points = []
        for i in range(len(self.trees)) :
            if self.variance_truth_value == True :
                print("intial_point : ",point)
                point = point[self.trees_data[i][1]]
                print("shuffle : ",self.trees_data[i][1],"\nfinal_point : " , point)
            nearest_points.append(self.trees[i].get_nearest(point)[0])


        return nearest_points
