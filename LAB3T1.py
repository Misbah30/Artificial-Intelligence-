def BFS():
    initial='D'
    final='F'
    graph={

        'A':['B','C','E'],
        'A':Node('A',None,['B','C','E'],None),
        'B':Node('B',None,['A','D','E'],None),
        'C':Node('C',None ,['A','F','G'],None),
        'D':Node('D',None,['B','E'],None),
        'E':Node('E',None,['A','B','D'],None),
        'F':Node('F',None,['C'],None),
        'G':Node('G',None,['C'],None)
        }
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m= queue.pop(0)
        print(m,end='')
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
queue.append(negihbour)
         
BFS(visited,graph,'A')
