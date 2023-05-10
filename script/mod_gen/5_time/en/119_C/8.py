def main():
    import sys
    import numpy as np
    import math
    import itertools
    import copy
    input = sys.stdin.readline
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10**6
    for i in itertools.product(range(4), repeat=N):
        a = []
        b = []
        c = []
        for j in range(N):
            if i[j] == 0:
                a.append(l[j])
            elif i[j] == 1:
                b.append(l[j])
            elif i[j] == 2:
                c.append(l[j])
        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            continue
        else:
            mp = 0
            mp += (len(a)-1)*10
            mp += (len(b)-1)*10
            mp += (len(c)-1)*10
            mp += abs(sum(a)-A)
            mp += abs(sum(b)-B)
            mp += abs(sum(c)-C)
            ans = min(ans, mp)
    print(ans)

if __name__ == '__main__':
    main()