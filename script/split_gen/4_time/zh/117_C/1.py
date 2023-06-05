def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n>=m:
        print(0)
        return
    if n==1:
        print(x[m-1]-x[0])
        return
    l = []
    for i in range(m-1):
        l.append(x[i+1]-x[i])
    l.sort(reverse=True)
    print(x[m-1]-x[0]-sum(l[:n-1]))
