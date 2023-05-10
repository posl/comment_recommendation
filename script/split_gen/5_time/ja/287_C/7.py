def main():
    n, m = map(int, input().split())
    path = [0] * n
    for i in range(m):
        u, v = map(int, input().split())
        path[u-1] += 1
        path[v-1] += 1
    print("Yes" if max(path) <= 2 else "No")
