graph={}
n=int(input("Enter the no.of nodes in graph-"))
for i in range(1,n+1):
    parent=input("Enter the node:")
    child=list(input("Enter the adjacent nodes:").split())
    graph[parent]=child
visited = []
queue = []

def BFS(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print (m, end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

start=input("Enter the starting node:")
print("Following is the Breadth-First Search")
BFS(visited, graph, start)
