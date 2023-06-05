def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    sum = [0 for _ in range(n)]
    sum[0] = a[0]
    for i in range(1,n):
        sum[i] = sum[i-1] + a[i]
    for i in range(q):
        idx = 0
        ans = 0
        while idx < n and a[idx] < x[i]:
            ans += a[idx]
            idx += 1
        if idx == n:
            print(sum[n-1] + (x[i] - a[n-1]) * n)
        else:
            print(ans + (n-idx)*x[i])
