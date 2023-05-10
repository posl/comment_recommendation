def main():
    n,m,x,t,d = map(int,input().split())
    for i in range(x,m):
        t += d
    print(t)
