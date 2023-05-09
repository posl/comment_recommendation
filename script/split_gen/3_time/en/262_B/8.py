def main():
    #Read the input
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    #Create a list of sets of connected vertices for each vertex
    neighbors = [set() for _ in range(N)]
    for u, v in edges:
        neighbors[u-1].add(v-1)
        neighbors[v-1].add(u-1)
    #Loop through each possible tuple of vertices
    count = 0
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                #Check if the vertices are connected
                if b in neighbors[a] and c in neighbors[b] and a in neighbors[c]:
                    count += 1
    print(count)
