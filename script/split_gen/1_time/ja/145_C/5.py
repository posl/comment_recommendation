def main():
    import sys
    import math
    import itertools
    N = int(sys.stdin.readline())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, sys.stdin.readline().split())
        x.append(x_i)
        y.append(y_i)
    xy = list(itertools.permutations(range(N)))
    ans = 0
    for i in xy:
        for j in range(N-1):
            ans += math.sqrt((x[i[j]]-x[i[j+1]])**2+(y[i[j]]-y[i[j+1]])**2)
    print(ans/len(xy))
