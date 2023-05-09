def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    s = sorted(p)
    for i in range(n):
        p[i] = s.index(p[i])+1
    print(*p)
