def main():
    n,m = map(int,input().split())
    u = [0]*m
    v = [0]*m
    for i in range(m):
        u[i],v[i] = map(int,input().split())
    print(n-1)
