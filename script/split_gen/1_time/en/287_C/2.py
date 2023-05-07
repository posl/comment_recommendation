def main():
    n, m = map(int, input().split())
    edges = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        edges[u-1].add(v-1)
        edges[v-1].add(u-1)
    if m != n - 1:
        print("No")
        return
    for i in range(n):
        if len(edges[i]) != 2:
            print("No")
            return
    print("Yes")
