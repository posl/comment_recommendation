def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(0,n):
        d.append(d[i]+l[i])
    for i in range(0,n+1):
        if d[i] > x:
            print(i)
            return
    print(n+1)
