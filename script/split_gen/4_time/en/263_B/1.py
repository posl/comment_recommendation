def generations(n, p):
    if n == 1:
        return 0
    else:
        return 1 + generations(p[n-1], p)
n = int(input())
p = [int(i) for i in input().split()]
print(generations(n, p))
