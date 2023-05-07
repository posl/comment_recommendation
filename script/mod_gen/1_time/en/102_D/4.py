def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i]+a[i])
    ans = 10**20
    for i in range(1,n-2):
        for j in range(i+1,n-1):
            ans = min(ans, abs(s[i] - s[0]-s[i]), abs(s[j] - s[i]-s[j]), abs(s[n] - s[j]-s[n]))
    print(ans)
    return

if __name__ == '__main__':
    main()