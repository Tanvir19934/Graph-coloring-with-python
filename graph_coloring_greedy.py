
'''this is a greedy algorithm for graph coloring problem. The goal is to
color the graph using minimum number of colors such that no adjacent nodes 
(or countries) is assigned the same color. The greedy algorithm first sorts
all the nodes in a descending order according to their degrees. That is, the node
with the highest number of neighbors is colored first. Then it simply 
assigns the smallest possible color to a node such that no conflict arises 
between thenode in consideration and its neighbors. Find the full problem description
in README'''



import pandas as pd
file_location = 'https://raw.githubusercontent.com/Tanvir19934/Graph-coloring-with-python/main/data/gc_70_1'
input_data = pd.read_csv(file_location, header = None)
import numpy as np
from collections import defaultdict



#parsing the input
input_data = input_data.iloc[:,0].str.split(' ')
node_count = int(input_data[0][0])
edge_count = int(input_data[0][1])
colors = [i for i in range(0,node_count)]
edges = list(input_data)
edges = edges[1:]
edges = np.array(edges,dtype=int)
unique_nodes = np.unique(edges) #creating a list of unique nodes present

# greedy solution
node_relations = {}
for j in unique_nodes:
  for i in range(0,edge_count):
    if edges[i][0]==j or edges[i][1]==j:
      node_relations.setdefault(j, []).append(edges[i])
      #node_relations[j].append(edges[i])  #wont work
      '''appending new elements to the list of keys. gotta use setdefault because 
      appending like this - node_relations[j].append(edges[i]), will generate an 
      error since the list does not exist at the beginning of append.'''
sorted_node_relations = sorted(node_relations, key= lambda x:len(node_relations[x]), reverse=True)
keys, values = node_relations.keys(), node_relations.values()
values = list(values) #this gives an array of neighbors of all the nodes
#sorting the nodes according to their degrees in descending order
assigned_colors = {}
for i in range(0,node_count):
  assigned_colors[i] = -1    #initializing colors as -1


def isSafe(i,color):

  '''this function checks if the tentative color of a node is already assigned 
  to its neighbors. If so, the function returns False. The function takes two
  arguements. i is the current node considered and color is its tentaively
  assigned color.'''
  neighbors = []
  for j in range(0,len(values[i])): #iterates through all the edges related to i
    if values[i][j][1]!=i:
      neighbors.append(values[i][j][1]) #separating i's neighbors and putting them in a list
    else:
      neighbors.append(values[i][j][0]) #separating i's neighbors and putting them in a list
  #print(neighbors)     #uncomment to see node i's neighbors
  for i in neighbors: #iterate through all the neighbors of i
    if assigned_colors[i]==color: #checks if any neighbor of i has the same color color
      return False
  return True

for i in sorted_node_relations: #iterate through the sorted nodes
  color = 1
  while(1):
    if isSafe(i,color) == True:
      assigned_colors[i]=color
      break
    else:
      color = color+1
# prepare the solution in the specified output format
output_data = str(max(assigned_colors.values())) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, assigned_colors.values()))
print(output_data)













