def solve():
    N = int(input())
    v = [int(x) for x in input().split()]
    v.sort()
    while len(v) > 1:
        x = v.pop(0)
        y = v.pop(0)
        v.append((x + y) / 2)
        v.sort()
    print(v[0])
