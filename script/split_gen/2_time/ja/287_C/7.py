def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    else:
        edge = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, input().split())
            edge[u - 1].append(v - 1)
            edge[v - 1].append(u - 1)
        for i in range(n):
            if len(edge[i]) != 2:
                print("No")
                return
        print("Yes")
