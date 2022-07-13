this is a greedy algorithm for graph coloring problem. The goal is to
color the graph using minimum number of colors such that no adjacent nodes 
(or countries) is assigned the same color. The greedy algorithm first sorts
all the nodes in a descending order according to their degrees. That is, the node
with the highest number of neighbors is colored first. Then it simply 
assigns the smallest possible color to a node such that no conflict arises 
between thenode in consideration and its neighbors <br />

**the input is in the form of-** <br /> <br />
nodes &nbsp; edges <br />
u_1 &nbsp; v_1 <br />
u_2 &nbsp; v_2 <br />
.............. <br />
.............. <br />
u_nodes &nbsp; v_nodes <br /> <br />
nodes = number of total nodes <br />
edges = number of total edges <br />
u_1 &nbsp; v_1 denotes that there is an arc between nodes u_1 and v_1, that is,
nodes u_1 and v_1 are neighbors. <br />
For example: <br />
4 &nbsp; 3 <br />
0 &nbsp; 1 <br />
1 &nbsp; 2 <br />
1 &nbsp; 3 <br />
means there are 4 nodes and 3 edges. node (0,1), (1,2), and (1,3) are neighbors. <br />  <br />
**The output is in the form of**- <br /> <br />
obj &nbsp; opt <br />
c_1 c_2.....................c_node <br /> <br />
obj = total number of colors used <br />
opt = a flag indicating whether the solution is optimal or not. opt = 0 if not 
optimal, opt = 1 if optimality is proven. <br />
c_1 is the assigned color of node 1 and so on... <br />
For example: <br />
5 0\n <br />
1 2 3 2 2 2 3 3 3 2 2 4 3 3 3 2 4 5 2 2 <br />
denotes 5 color is needed in total. the solution is not proven to be
optimal. the second line denotes the assigned color of each node'''
