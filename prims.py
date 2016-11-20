from collections import defaultdict
from heapq import *

def prims(g):
  
  g = graph
  

  mst=[]    
  initial=1
  visited=set()    
  visited.add(initial)
  unvisited_edges=graph[1][:]
  heapify(unvisited_edges) 
  total_weight = 0
  while unvisited_edges:
            
         weight,n1,n2=heappop(unvisited_edges)
                  
         if n2 not in visited:
             visited.add(n2)
             
             mst.append((n1,n2,weight))
             total_weight += weight
             for edge in graph[n2]:
                 if edge[2] not in visited:
                     heappush(unvisited_edges,edge)
  
  return mst                   
      
    
n,m = map(int,raw_input().strip().split())
graph = defaultdict(list)
for i in range(m):
    n1,n2,w = map(int,raw_input().strip().split())
    graph[n1].append((w,n1,n2))
    graph[n2].append((w,n2,n1))

print prims(graph)
        
