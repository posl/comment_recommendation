def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    for i in range(n):
        if len(g[i]) > 2:
            print("No")
            return
    print("Yes")
