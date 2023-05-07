def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
        for j in range(i):
            b[i] = max(b[i],b[j] + a[i-j-1])
    print(max(b))
