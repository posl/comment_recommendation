def solve():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p[-1] = p[-1] / 2
    print(int(sum(p)))
