parent={}
rank={}

def make_set(vertex):
    
    parent[vertex]=vertex
    rank[vertex]=0

def find(vertex):
    
    if parent[vertex]!=vertex:
        return find(parent[vertex])
    else:
      return vertex

def union(vertex1,vertex2):
    
    root1=find(vertex1)
    root2=find(vertex2)
    
    if rank[root1]>rank[root2]:
        parent[root2]=root1
    else:
        parent[root1]=root2
        if rank[root1]==rank[root2]:
             rank[root2]+=1
         
      
def kruskals(edges,vertices):
    
    edges.sort() 
    mst=set()
    for vertex in vertices:
        make_set(vertex)
    for edge in edges:
        weight,vertex1,vertex2=edge
       
        if find(vertex1)!= find(vertex2):
            mst.add(edge)
            union(vertex1,vertex2)
            
    return mst








if __name__=="__main__":


    edges =  [(7, 'A', 'B'),
              (5, 'A', 'D'),
              (8, 'B', 'C'),
              (9, 'B', 'D'),
              (7, 'B', 'E'),
              (5, 'C', 'E'),
              (15, 'D', 'E'),
              (6, 'D', 'F'),
              (8, 'E', 'F'),
              (9, 'E', 'G'),
              (11, 'F', 'G')]
              
    vertices=['A','B','C','D','E','F','G']
    print kruskals(edges,vertices)        