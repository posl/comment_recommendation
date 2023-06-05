def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    s = [0]
    for i in range(1, n+1):
        s.append(s[i-1]+a[i])
    ans = 0
    sum = {}
    for i in range(1, n+1):
        if s[i]-k in sum:
            ans += sum[s[i]-k]
        if s[i] in sum:
            sum[s[i]] += 1
        else:
            sum[s[i]] = 1
    print(ans)

if __name__ == '__main__':
    main()