def main():
    n = int(input())
    a = list(map(int, input().split()))
    #累積和
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    #最小値の累積和
    min_s = [0] * (n+1)
    min_s[0] = s[0]
    for i in range(1, n+1):
        min_s[i] = min(min_s[i-1], s[i])
    #最大値の累積和
    max_s = [0] * (n+1)
    max_s[0] = s[0]
    for i in range(1, n+1):
        max_s[i] = max(max_s[i-1], s[i])
    ans = 10**9
    for i in range(3, n-1):
        ans = min(ans, max(max_s[i]-min_s[i], max_s[n]-max_s[i], max_s[i]-min_s[i], max_s[n]-max_s[i]) - min(max_s[i]-min_s[i], max_s[n]-max_s[i], max_s[i]-min_s[i], max_s[n]-max_s[i]))
    print(ans)

if __name__ == '__main__':
    main()