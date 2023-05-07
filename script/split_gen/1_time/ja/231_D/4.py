def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    if m == 0:
        print("Yes")
        return
    for i in range(n):
        if len(g[i]) == 1:
            print("Yes")
            return
    print("No")
