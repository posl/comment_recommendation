def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n == 1:
        print(abs(x[0]-x[m-1]))
    else:
        x1 = x[0]
        x2 = x[n-1]
        m
