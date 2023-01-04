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



#Code for maze
class Node :

    def __init__(self,state,parent,actions,cost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.cost=cost  
def BFSCost():
    inital="START"
    goal="GOAL"
    
    graph={
        'START' : Node('START',None,['A'],[] ),
        'A' : Node('A','START',['START','B'],[]),
        'B' : Node('B','A',['A','C'],[] ),
        'C' : Node('C','B',['B','D','V'] ,[]),
        'D' : Node('D','C',['C','E'],[] ),
        'E' : Node('E','D',['D','F'],[] ),
        'F' : Node('F','E',['E','G'],[] ),
        'G' : Node('G','F',['F','H',],[] ),
        'H' : Node('H','G',['G','I'],[] ),
        'I':Node('I','H',['H','J'],[]),
        'J':Node('J','I',['I','K'],[]),
        'K':Node('K','J',['J','L'],[]),
        'L':Node('L','K',['K','M'],[]),
        'M' : Node('M','L',['N','L'],[120,75] ),
        'N' : Node('N','M',['GOAL','M','0'],[138,146] ),
        'O' : Node('O','N',['N','P'],[86] ),
        'P' : Node('P','O',['O','R'],[142,92] ),
        'Q' : Node('Q','R',['R'],[92,87] ),
        'R' : Node('R','P',['Q','S'],[]),
        'S' : Node('S','R',['R','U'],[] ),
        'T' : Node('T','U',['W','U'],[] ),
        'U' : Node('U','S',['S','T','X'],[] ),
        'V' : Node('V','C',['C','W'],[] ),
        'W' : Node('W','T',['V','T','X'],[] ),
        'X' : Node('X','U',['W','U'],[] ),
        'GOAL' : Node('GOAL','N',['N'],[] ),
        }
    front=[inital]
    exp=[]
   
    while(len(front)!=0) : 
          cNode=front.pop(0)
          exp.append(cNode)
          
          if cNode==goal:
              break
          for i in graph[cNode].actions :
              if i not in front and i not in exp : 
                  graph[i].parent==cNode
                  if graph[i].state==goal:
                      return actionSequence(graph,inital,goal)
                  front.append(i)
def actionSequence(graph,inital,goal):
    sol=[goal]
    cp=graph[goal].parent
    while cp!=None:
        sol.append(cp)
        cp=graph[cp].parent
    sol.reverse()
    return sol
sol=BFSCost()
print(sol)



#Activity
class Node :

    def __init__(self,state,parent,actions,cost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.cost=cost
def BFSCost():
    inital="Arad"
    goal="Neamt"
    graph={
        'Oradea' : Node('Oradea',None,['Zerind','Sibiu'],[71,151] ),
        'Zerind' : Node('Zerind',None,['Arad', 'Oradea'],[75,71 ]),
        'Arad' : Node('Arad',None,['Zerind','Timisoara','Sibiu'],[75,118,140] ),
        'Sibiu' : Node('Sibiu',None,['Fagaras','Rimnicu Vilcea','Oradea','Arad'],[99,80,151,140] ),
        'Fagaras' : Node('Fagaras',None,['Sibiu','Bucharest'],[99,211] ),
        'Bucharest' : Node('Bucharest',None,['Fagaras','Pitesti','Urziceni','Giurgiu'],[211,101,85,90] ),
        'Pitesti' : Node('Pitesti',None,['Rimnicu Vilcea','Bucharest','Craiova'],[97,101,138] ),
        'Urziceni' : Node('Urziceni',None,['Bucharest','Hirsova','Vaslui'],[85,98,142] ),
        'Hirsova' : Node('Hirsova',None,['Urziceni','Eforie'],[98,86] ),
        'Timisoara':Node('Timisoara',None,['Lugoj','Arad'],[111,118]),
        'Lugoj':Node('Lugoj',None,['Mehadia','Timisoara'],[70,111]),
        'Mehadia':Node('Mehadia',None,['Drobeta','Lugoj'],[75,70]),
        'Rimnicu Vilcea':Node('Rimnicu Vilcea',None,['Sibiu','Pitesti'],[70,111]),
        'Drobeta' : Node('Drobeta',None,['Craiova','Mehadia'],[120,75] ),
        'Craiova' : Node('Craiova',None,['Pitesti','Rimnicu Vilcea'],[138,146] ),
        'Eforie' : Node('Eforie',None,['Hirsova'],[86] ),
        'Vaslui' : Node('Vaslui',None,['Urziceni','Iasi'],[142,92] ),
        'Iasi' : Node('Iasi',None,['Vaslui','Neamt'],[92,87] ),
        'Giurgiu' : Node('Giurgiu',None,[],[]),
        'Neamt' : Node('Neamt',None,[],[] ),
        }
    front=[inital]
    exp=[]
   
    while(len(front)!=0) : 
          cNode=front.pop(0)
          exp.append(cNode)
          print (cNode)
          for i in graph[cNode].actions :
              if i not in front and i not in exp:
                  graph[i].parent==cNode
                  if graph[i].state==goal:
                      return actionSequence(graph,inital,goal)
                  front.append(i)
def actionSequence(graph,inital,goal):
    sol=[goal]
    cp=graph[goal].parent
    while cp!=None:
        sol.append(cp)
        cp=graph[cp].parent
    sol.reverse()
    return sol
sol=BFSCost()
print(sol)
