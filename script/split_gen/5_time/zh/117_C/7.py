def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n == 1:
        print(x[-1]-x[0])
        return
    else:
        dis = [0]*(m-1)
        for i in range(m-1):
            dis[i] = x[i+1]-x[i]
        dis.sort()
        print(sum(dis[:m-n]))
