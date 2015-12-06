
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import os
from sklearn.cross_validation import train_test_split
import random
import math
import scipy
import collections
from sklearn.metrics import confusion_matrix,accuracy_score
path = os.getcwd()

ADJ = pd.read_csv(path+'/ADJ.csv',index_col=0)
ADJ.columns = [int(col.strip('V')) for col in ADJ.columns]
click = pd.read_csv(path+'/click.csv',index_col=0)
click.columns = [int(col.strip('V')) for col in click.columns]
X_ad = pd.read_csv(path+'/X_ad.csv',index_col=0)
X_user = pd.read_csv(path+'/X_user.csv',index_col=0)

"""X_user = X_user[:100]
click = click[:100]
ADJ = ADJ.loc[1:100,1:100]"""

def normalize_attributes():
    # normalize the user demographics and attributes
    X_user['age'] = X_user.apply(lambda x : (x[0] - np.min(X_user.age))/(np.max(X_user.age) - np.min(X_user.age)),axis=1)
    X_user['edu'] = X_user.apply(lambda x : (x[2] - np.min(X_user.edu))/(np.max(X_user.edu) - np.min(X_user.edu)),axis=1)
    X_user['income'] = X_user.apply(lambda x : (x[3] - np.min(X_user.income))/(np.max(X_user.income) - np.min(X_user.income)),axis=1)

normalize_attributes()

def distance_matrix(size):
    '''returns the euclidean matrix between all pair users by (age,gender,income,degree of connection)'''
    dist_matrix = np.zeros((size,size))
    for k in range(0,size):
        for i in range(0,size):
            degree_of_connection = degree_mat[k+1][i+1]
            v1 = np.append(np.array(X_user.loc[k+1,:]),1)
            if degree_of_connection == 0:
                v2 = np.append(np.array(X_user.loc[i+1,:]),1.)
            else:
                v2 = np.append(np.array(X_user.loc[i+1,:]),degree_of_connection)
            dist_matrix[k][i] = scipy.spatial.distance.euclidean(v1, v2)
    return dist_matrix

degree_mat = pd.read_csv(path+'/dist_matrix.csv',header=None)
degree_mat.columns = [_ for _ in range(1,1001)]
degree_mat.index = np.arange(1, len(degree_mat) + 1)
distance_matrix = distance_matrix(1000)


def neighbour_set_dfs(idx):
    
    '''returns the connected graph of the candidate'''
    
    def user_graph():
        
        '''Returns the graph (adjacency list) of the user network'''
    
        graph = dict()
        
        for i in range(1,1001):
            graph[i] = set(list(ADJ.columns[ADJ.loc[i,:] == 1]))
        return graph

    def dfs(graph, start, visited=None):
        
        '''Returns the total connected components (list) of the given user in his/her network'''
        '''credits: Eddmann'''
    
        if visited is None:
            visited = set()
        visited.add(start)
        for next in graph[start] - visited:
            dfs(graph, next, visited)
        return visited

    return dfs(user_graph(),idx)


"""user_id = 1
ad_test = click[:user_id] # user 1 has viewd 84% of the ad's
ad_test = ad_test.dropna(axis=1)"""

def social_network(user_id,k):
    
    '''Returns the pruned social network which has the user_ids with highest predictive power'''

    unpruned = list(neighbour_set_dfs(user_id))
    sim_dict = dict()
    pruned = list()
    
    for i in range(len(unpruned)):
        sim_dict[unpruned[i]] = distance_matrix[user_id-1,unpruned[i]-1]
    
    sorted_sim_dict = sorted(sim_dict.items(), key=lambda x: (-x[1], x[0]),reverse=True)
    
    for _ in range(1,k+1):
        pruned.append(sorted_sim_dict[_][0])
        
    return pruned

# The idea: Find the average click-through rate of your social network
# If the rate of for a particular ad is higher than the average click through of your network, then there is a 
# higher chance of you clicking

def social_network_clickthrough(user_id,k):
    """
    Finding the average click-through rate of your social network
    """
    close_friends = social_network(user_id,k)
    overall_rate = list()
    for friend in close_friends:
        friend_clicks = np.sum(click.loc[friend,:][~np.isnan(click.loc[friend,:])])
        friend_totalclicks = len(click.loc[friend,:][~np.isnan(click.loc[friend,:])])
        friend_rate = (friend_clicks/friend_totalclicks)*1.
        overall_rate.append(friend_rate)
    return np.mean(overall_rate)

k = 15
final = dict()

for user_id in list(click.index):
    #ads = list(click.loc[user_id,:][~np.isnan(click.loc[user_id,:])].index)
    ads = list(click.loc[user_id,:].index)
    friends_list = social_network(user_id,k)
    overall_rate = social_network_clickthrough(user_id,k)
    preds = list()

    for ad_id in ads:
        reduce_friends_list = filter(lambda x : x in click.loc[:,ad_id][~np.isnan(click.loc[:,ad_id])].index,friends_list)
        clicks = np.sum(click.loc[reduce_friends_list,ad_id][~np.isnan(click.loc[reduce_friends_list,ad_id])])
        total = len(click.loc[reduce_friends_list,ad_id][~np.isnan(click.loc[reduce_friends_list,ad_id])])
        rate = (clicks/total)*1.
        if rate >= overall_rate:
            preds.append(1)
        else:
            preds.append(0)

    final[user_id] = preds

#print len(ads),len(preds)
#accuracy_score(list(click.loc[user_id,:][~np.isnan(click.loc[user_id,:])]),preds)

submission = pd.DataFrame(final).transpose()


# In[ ]:



