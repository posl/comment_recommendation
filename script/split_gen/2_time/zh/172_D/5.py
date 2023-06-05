def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(1,n):
        a[i] += a[i-1]
    for i in range(1,m):
        b[i] += b[i-1]
    ans = 0
    j = m
    for i in range(n+1):
        if a[i] > k:
            break
        while j > 0 and b[j-1] > k - a[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)
