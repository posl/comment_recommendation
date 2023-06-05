def problem115_b():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    p[0] /= 2
    print(int(sum(p)))
