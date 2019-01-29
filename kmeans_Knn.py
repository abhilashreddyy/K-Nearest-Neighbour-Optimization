# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:11:10 2018

@author: abhi
"""
# please excuse me for so many print statements because i used them for debugging

   
from sklearn.cluster import KMeans
import heapq
import common_function as cf

class node(object) :
    def __init__(self,mean,lable=None,point = None):
        self.mean = mean
        self.child = []
        self.points = point
        self.lable = lable
        
        
class nary_tree(object) :
    def __init__(self,points,y,k,no_of_comparisions,clustring_iteration) :
        self.k = k
        self.traverse_pq = []
        self.dictionary = {}
        self.final_pq = []
        self.count = 0
        self.no_of_comparisions = no_of_comparisions
        self.clustring_iteration = clustring_iteration
        #plt.scatter([val[0] for val in items],[val[1] for val in items],marker = "X",color = "red") 
        
        self.points = points
        self.y = y
        
        self.id = 1
        
        
        
        #self.samp_trav(self.root)
    def make_tree(self) :
        self.root = self.make_KMeans_tree(self.points,self.y,None,0)
        
    def get_nearest(self,point) :
        self.traverse_pq = []
        self.final_pq = []
        self.count = 0
        return self.SearchKMeansTrees(point)
    
    # this function builds tree with k-means cluster   
    def make_KMeans_tree(self,cluster,y,mean,depth) :
        model = KMeans(n_clusters = self.k,max_iter = self.clustring_iteration,init = "random",n_init = 1,tol = 1e-6,precompute_distances = False,algorithm = "full")

        root = node(mean)
        model.fit(cluster)
            
        for i,mean in enumerate(model.cluster_centers_) :
            
            temp_cluster = [cluster[j] for j,val in enumerate(model.labels_) if val == i]
            #print(len(model.labels_),len(y))
            temp_y = []
            for j,val in enumerate(model.labels_) :
                if val == i :
                    #print(len(model.labels_),j,len(y),len(cluster))
                    temp_y.append(y[j])
                    
            #temp_y = [y[j] for j,val in enumerate(model.labels_) if val == i]
            #print("y_length : ",temp_y,"\ncluster_len : ",temp_cluster)
            #print(model.labels_,"\n",cluster,"\n",temp_cluster,"\n",depth,"\n","\n")
            #print(len(temp_cluster)," ",self.k," ",i,temp_cluster," ",depth,"\n\n")
            if len(temp_cluster) > self.k :
                #print("leaf")
                #print("non-leaf : ","\n",mean,"\n",cluster,"\n",depth+1)
                
                root.child.append(self.make_KMeans_tree(temp_cluster,temp_y,mean,depth+1))
            elif temp_cluster !=[]:
                #print("non-leaf")
                #print("leaf : ","\n",mean,"\n",cluster,"\n",depth+1)
                root.child.append(node(mean,temp_y,point = temp_cluster))
        return root   
    
    # this function searches kmeans tree we build from above function
    def SearchKMeansTrees(self,point) :
        self.count = 0
        self.TraverseKMeansTree(self.root,point)
        while len(self.traverse_pq) > 0 :
            try :
                
                q = heapq.heappop(self.traverse_pq)
                temp_node = self.dictionary[q[1]]
                
                #print("heap_pop : " ,q )
                self.TraverseKMeansTree(temp_node,point)
                del self.dictionary[q[1]]
            except :
                print("except")
        #print(len(self.final_pq))
        #print(self.final_pq)
        #req = []
        #for i in range(n) :
        #    val = heapq.heappop(self.final_pq)
        #    req.append(val)
            #print(val)
        return self.final_pq
    
    # this function traverse kmeans tree while searching
    def TraverseKMeansTree(self,root,main_point) :
        if self.no_of_comparisions > self.count :
            if root.points != None :
                
                for temp_point,temp_y in zip(root.points,root.lable) :  
                    #print(temp_point)
                    
                    heapq.heappush(self.final_pq,(cf.EuclideanDistance(main_point,temp_point),(temp_point,temp_y)))
                self.count = self.count + len(root.points)
            elif root.points == None :
                arr = []
                for c_node in root.child :
                    self.dictionary[self.id] = c_node
                    arr.append((cf.EuclideanDistance(main_point,c_node.mean),self.id))
                    self.id += 1
                arr.sort(key=lambda x :x[0])
                #print(arr)
                
                self.TraverseKMeansTree(self.dictionary[arr[0][1]],main_point)
                del self.dictionary[arr[0][1]]
                
                
                for val in arr[1:] :
                    heapq.heappush(self.traverse_pq,val)
            
    def samp_trav(self,root) :
        if root.child == [] :
            for temp_point in root.points :  
                print(temp_point)
        else :
            for c_node in root.child :
                self.samp_trav(c_node)
        
        

    

    