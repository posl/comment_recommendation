def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(n-1):
        sum += a[i]
    if n*m - sum > k:
        print(-1)
    elif n*m - sum < 0:
        print(0)
    else:
        print(n*m - sum)
