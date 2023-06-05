def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(41,-1,-1):
        x = 1 << i
        cnt = 0
        for j in range(n):
            if a[j] & x:
                cnt += 1
        if cnt < n-cnt and ans + x <= k:
            ans += x
    sum = 0
    for i in range(n):
        sum += ans ^ a[i]
    print(sum)
main()
