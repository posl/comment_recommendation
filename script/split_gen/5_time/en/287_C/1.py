def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        u, v = map(int, input().split())
        if u not in d:
            d[u] = 1
        else:
            d[u] += 1
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1
    for v in d:
        if d[v] > 2:
            print("No")
            return
    print("Yes")
