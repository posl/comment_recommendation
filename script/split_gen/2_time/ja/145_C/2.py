def main():
    import math
    import itertools
    import sys
    input = sys.stdin.readline
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        x, y = map(int, input().split())
        X[i] = x
        Y[i] = y
    dist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = math.sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)
    ans = 0
    for v in itertools.permutations(range(N)):
        for i in range(N-1):
            ans += dist[v[i]][v[i+1]]
    print(ans/math.factorial(N))
