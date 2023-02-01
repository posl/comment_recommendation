#Problem Statement
#You are given a simple undirected graph with N vertices numbered 1 to N and M edges numbered 1 to M. Edge i connects vertex u_i and vertex v_i.
#Find the number of connected components in this graph.
#
#Notes
#A simple undirected graph is a graph that is simple and has undirected edges.
#A graph is simple if and only if it has no self-loop or multi-edge.
#A subgraph of a graph is a graph formed from some of the vertices and edges of that graph.
#A graph is connected if and only if one can travel between every pair of vertices via edges.
#A connected component is a connected subgraph that is not part of any larger connected subgraph.
#
#Constraints
#1≤N≤100
#0≤M≤ N(N−1)/2
#1≤u_i,v_i≤N
#The given graph is simple.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#u_1 v_1
#u_2 v_2 
#⋮
#u_M v_M
#
#Output
#Print the answer.
#
#Sample Input 1
#5 3
#1 2
#1 3
#4 5
#
#Sample Output 1
#2
#
#Sample Input 2
#5 0
#
#Sample Output 2
#5
#
#Sample Input 3
#4 6
#1 2
#1 3
#1 4
#2 3
#2 4
#3 4
#
#Sample Output 3
#1

def main():
    N, M = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for i in range(M):
        u, v = list(map(int, input().split()))
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    print(solve(N, G))

def solve(N, G):
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for u in G[v]:
                stack.append(u)
    return ans

if __name__ == '__main__':
    main()