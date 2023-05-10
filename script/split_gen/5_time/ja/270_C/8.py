def main():
    n,x,y = map(int,input().split())
    s = [0] * (n+1)
    for i in range(n-1):
        u,v = map(int,input().split())
        s[u] += 1
        s[v] += 1
    if s[x] < s[y]:
        x,y = y,x
    print(x,y)
    return
