from collections import deque

def ford_fulkerson(G,source,sink):
    max_flw = 0
    all_paths,path_flws = [],[]
    while True:
        paths = bfs(G,source,sink)
        if not paths:
            break
        for path in paths:
            path_flw = min([G[path[i]][path[i+1]] for i in range(len(path)-1)])
            all_paths.append(path)
            max_flw += path_flw
            path_flws.append(path_flw)
            G = modify(G,path,path_flw)
    return max_flw, all_paths,path_flws

def modify(G,path,flw):
    for i in range(len(path)-1):
        u,v = path[i],path[i+1]
        G[u][v] -=  flw
        G[v][u] += flw
    return G 





def bfs(G,source,sink):
    paths =[]
    queue = deque([(source,[source])])
    while queue:
        u, path = queue.popleft()
        for v,capacity in enumerate(G[u]):
            if v not in path and capacity > 0:
                if v == sink:
                    paths.append(path+[v])
                else:
                    queue.append((v,path+[v]))
    return paths

#        D   M   K   B  P  s
G =     [[0, 8, 14, 0, 0, 0],
         [0, 0, 14, 12, 0, 0],
         [0, 6, 0, 0, 10, 0],
         [0, 0, 10, 0, 0, 17],
         [0, 0, 0, 7, 0, 6],
         [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5

max_flw,all_paths,path = ford_fulkerson(G,source,sink)
print(max_flw)
