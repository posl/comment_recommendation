def main():
    n,q = map(int,input().split())
    p = list(range(n+1))
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def union(x,y):
        px,py = find(x),find(y)
        if px != py:
            p[px] = py
    def same(x,y):
        return find(x) == find(y)
    ans = []
    for _ in range(q):
        c,*q = map(int,input().split())
        if c == 1:
            x,y = q
            union(x,y)
        elif c == 2:
            x,y = q
            if same(x,y):
                union(x,y-1)
                union(x+1,y)
        else:
            x = q[0]
            ans.append([i for i in range(1,n+1) if same(x,i)])
    for i in ans:
        print(len(i),*i)
