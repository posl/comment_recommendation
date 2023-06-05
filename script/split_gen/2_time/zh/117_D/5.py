def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    # print(x)
    if n >= m:
        print(0)
        return
    if n == 1:
        print(x[m-1]-x[0])
        return
    # print(x)
    # print(x[n-1]-x[0])
    # print(x[m-1]-x[n])
    # print(min(x[m-1]-x[0],x[n-1]-x[0],x[m-1]-x[n]))
    print(min(x[m-1]-x[0],x[n-1]-x[0],x[m-1]-x[n]))
main()
