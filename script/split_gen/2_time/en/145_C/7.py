def solve():
    N = int(input())
    x_y = [list(map(int, input().split())) for _ in range(N)]
    from itertools import permutations
    from math import sqrt
    ans = 0
    for p in permutations(range(N)):
        for i in range(N-1):
            ans += sqrt((x_y[p[i]][0]-x_y[p[i+1]][0])**2 + (x_y[p[i]][1]-x_y[p[i+1]][1])**2)
    print(ans/len(list(permutations(range(N)))))
