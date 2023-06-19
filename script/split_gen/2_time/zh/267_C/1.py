def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    print(b)
    print(max(b[i+j]-b[i]+a[i]*(j+1) for i in range(n-m+1) for j in range(m)))
