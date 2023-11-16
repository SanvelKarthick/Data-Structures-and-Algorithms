graph={}
n=int(input("Enter the no.of nodes in graph-"))
for i in range(1,n+1):
    parent=input("Enter the node:")
    child=list(input("Enter the adjacent nodes:").split())
    graph[parent]=child
visited=[]


def DFS(graph, start, visited):
    visited.append(start)
    print(start)
    for ne in graph[start]:
        if ne not in visited:
            DFS(graph, ne, visited)
    return visited

start=input("Enter the starting node:")
print("Following is the Depth-First Search")
DFS(graph,start,visited)
