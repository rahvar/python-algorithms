from collections import defaultdict
from heapq import *

def prims(edges,nodes):
  
  graph=defaultdict(list)
  
  for v1,v2,w in edges:
      graph[v1].append((w,v1,v2))
      graph[v2].append((w,v2,v1))
  mst=[]    
  initial=nodes[0]
  visited=set()    
  visited.add(initial)
  unvisited_edges=graph[nodes[0]][:]
  heapify(unvisited_edges) 
  
  while unvisited_edges:
            
         weight,n1,n2=heappop(unvisited_edges)
                  
         if n2 not in visited:
             visited.add(n2)
             
             mst.append((n1,n2,weight))
             
             for edge in graph[n2]:
                 if edge[2] not in visited:
                     heappush(unvisited_edges,edge)
  
  return mst                   
      
    
if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]    
    nodes=["A","B","C","D","E","F","G"]
    
    print prims(edges,nodes)
        
