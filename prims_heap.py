
from collections import defaultdict



INF = 9999999

class Heap:
    def __init__(self):
        self.heap = [0]
        self.dic = dict()
    def heap_push(self,value,tup=[]):
        self.heap = self.heap + [value]
        l = len(self.heap) -1
        if tup:
            self.dic[l] = tup
        self.heapify_up(l)

    def heapify_up(self,i):
        while i>1:
            j = int(i/2)
            if self.heap[i]<self.heap[j]:
                a = self.heap[i]
                b = self.heap[j]
                self.heap[i],self.heap[j] = b,a
                self.dic[i],self.dic[j] = self.dic[j],self.dic[i]
                i = j
            else:
                break
    def heap_pop(self):
        val = self.heap[1]
        pairs = self.dic[1]
        self.heap[1] = self.heap[-1]
        self.dic[1] = self.dic[len(self.heap)-1]
        l = len(self.heap)
        self.heap  =self.heap[0:l-1]
        self.heapify_down(1)
        res =  [val] + [pairs] 
        return res

    def heapify_down(self,i):
        x = 2*i
        l = len(self.heap)-1
        while x<=l:
            if x==l or self.heap[x]<=self.heap[x+1]:
                j =x
            else:
                j = x+1
            if self.heap[j]<self.heap[i]:
                self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
                self.dic[i],self.dic[j] = self.dic[j],self.dic[i]
                i = j
                x = 2*i
            else:
                break

    def is_empty(self):
        if len(self.heap)<=1:
            return True
        else:
            return False
    def print_heap(self):
        print self.heap






def prims(g):
  
  g = graph
  

  mst=[]  

  initial=1
  visited=set()    
  visited.add(initial)
  unvisited_edges=graph[1][:]
  trace = dict()
  total_weight = 0
  heap = Heap()
  for edge in unvisited_edges:
    wt = edge[0]
    d[edge[2]] = wt
    nodes = edge[1],edge[2]
    trace[edge[2]] = edge[1]    
    heap.heap_push(wt,edge[2])

  heap.print_heap()
  while not heap.is_empty():
            
         weight,n=heap.heap_pop()
         #print n,          
         if n not in visited:
             
             visited.add(n)
             y = n
             x = trace[n]
             x,y = sorted((x,y))
             print weight,x,y,'test'
             mst.append((x,y,weight))
             total_weight += weight
             for edge in graph[n]:

                 if edge[2] not in visited:
                    weight = edge[0]
                    if edge[2] ==2:
                      print d[edge[2]]
                    if weight<d[edge[2]]:
                     d[edge[2]] = weight   
                     trace[edge[2]] = edge[1]
                     nodes = edge[1],edge[2]
                     heap.heap_push(weight,edge[2])
 
  return mst,total_weight                   
      

f = open('input.txt','r')
n,m = map(int,f.readline().strip().split())
#n,m = map(int,raw_input().strip().split())
graph = defaultdict(list)
d = dict()
for i in range(1,n+1):
    d[i] = INF
for i in range(m):
    #n1,n2,w = map(int,raw_input().strip().split())
    n1,n2,w = map(int,f.readline().strip().split())
    graph[n1].append((w,n1,n2))
    graph[n2].append((w,n2,n1))

mst,wt = prims(graph)

 

#for i in range(n-1):
#    print mst[i],"-",act_mst[i]

