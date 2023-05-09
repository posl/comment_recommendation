def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = [0]
    for i in range(n):
        sum_a.append(sum_a[i]+a[i])
    ans = 0
    for i in range(n+1):
        for j in range(i+1,n+1):
            if sum_a[j] - sum_a[i] >= k:
                ans += 1
    print(ans)
