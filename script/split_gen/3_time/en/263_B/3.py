def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    d = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        d[i] = d[p[i]] + 1
    print(max(d))
