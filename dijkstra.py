from collections import defaultdict
from heapq import *

INF=9999999
def dijkstra(graph,nodes,initial):
    g=defaultdict(list)
    for s,d,c in graph:
        g[s].append((d,c))
    dis={}
    
    for ver in nodes:  
        dis[ver]=INF
    dis[initial]=0
    
    visited=set()
    unviNodes=[(0,initial)]
    while unviNodes:
        (weight,node)=heappop(unviNodes)
        if node not in visited:
            visited.add(node)
            for ver,path_wt in g[node]:                

                dist=weight+path_wt                
                if dist<dis[ver]:
                    dis[ver]=dist
                    heappush(unviNodes,(dist,ver))
    return dis 
       
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
    
    print dijkstra(edges,nodes,"A")
    