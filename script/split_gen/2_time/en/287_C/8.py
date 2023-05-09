def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    edge = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    for i in range(1, n + 1):
        if len(edge[i]) != 2:
            print("No")
            return
    print("Yes")
