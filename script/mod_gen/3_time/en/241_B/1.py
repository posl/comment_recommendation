def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] >= B[j]:
            j += 1
        i += 1
    if j == M:
        print('Yes')
    else:
        print('No')
main()
This is my first post on this blog. I will try to write a post every week or so.
Here is my solution to the problem “The World is a Theatre” from the 2018 ICPC World Finals. This problem was a very difficult problem, and I was not able to solve it during the contest. However, I was able to solve it after the contest.
The problem is as follows:
You are given a directed graph with N vertices and M edges. The vertices are numbered from 0 to N-1. The edges are numbered from 0 to M-1. Each edge has a color, which is either red or blue. Your task is to find a red path from vertex 0 to vertex N-1, where a path is a sequence of edges such that the i-th edge is incident to the i-th vertex in the path. Note that the path can contain loops, and it does not have to be simple.
The input is given as follows:
N M
C_0 U_0 V_0
C_1 U_1 V_1
...
C_{M-1} U_{M-1} V_{M-1}
Here, C_i is the color of the i-th edge, and U_i and V_i are the endpoints of the i-th edge. Note that the graph is undirected, so the edge (U_i, V_i) is the same as the edge (V_i, U_i). The colors are given as follows:
0: red
1: blue
The output should be a single integer k, where k is the number of edges in your red path. If there is no red path, output −1 instead.
Constraints
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
0 ≤ C_i ≤ 1
0 ≤ U_i, V_i < N
The input is guaranteed to

if __name__ == '__main__':
    main()