def main():
    import sys
    import math
    import itertools
    import collections
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2))
    print(ans)

if __name__ == '__main__':
    main()