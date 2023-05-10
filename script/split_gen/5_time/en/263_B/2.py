def main():
    n = int(input())
    p = list(map(int, input().split()))
    g = [0] * n
    for i in range(n):
        if p[i] == 0:
            continue
        g[i] = g[p[i]-1] + 1
    print(max(g))
