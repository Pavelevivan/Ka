import math


def algorythm_ford_bellman(graph, start):
    previous = [start] * len(graph)
    previous[start] = -1
    for k in range(0, len(graph) - 1):
        for node in range(0,len(graph)):
            if node == start:
                continue
            for next_node in range(0, len(graph)):
                if graph[start][next_node] + graph[next_node][node] < graph[start][node]:
                    graph[start][node] = graph[start][next_node] + graph[next_node][node]
                    previous[node] = next_node
    return previous


if __name__ == '__main__':
    graph = []
    with open("in.txt") as f:
        nodes_num = int(f.readline())
        graph = [[]] * nodes_num
        for x in range(0, nodes_num):
            adj = f.readline().split(" ")
            connected = [math.inf] * nodes_num
            connected[x] = 0
            for y in range(0, len(adj), 2):
                node = int(adj[y])
                if node != 0:
                    coast = int(adj[y+1])
                    connected[node-1] = coast
            graph[x] = connected
        start = int(f.readline()) - 1
        target = int(f.readline()) - 1
    # print(nodes_num, graph, start, target)
    previous = algorythm_ford_bellman(graph, start)
    if graph[start][target] < math.inf:
        i = target
        path = []
        while i != start:
            path.append(i + 1)
            i = previous[i]
        path.append(start + 1)
        path.reverse()
        with open("out.txt", 'w') as f:
            f.write("YES\n")
            for x in range(0, len(path) - 1):
                f.write(str(path[x]) + " ")
            f.write(str(path[-1]) + "\n")
            f.write(str(graph[start][target]))
            # print(path, "path")
    else:
        with open("out.txt", 'w') as f:
            f.write("NO")
    # print(graph)
    # i = input()
