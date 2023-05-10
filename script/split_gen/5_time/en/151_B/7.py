def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    x = m*n
    y = sum(a)
    z = x - y
    if z > k:
        print(-1)
    elif z <= 0:
        print(0)
    else:
        print(z)
