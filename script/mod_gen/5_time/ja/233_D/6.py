def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0] * (n+1)
    s[0] = 0
    for i in range(n):
        s[i+1] = s[i] + a[i]
    from collections import Counter
    c = Counter(s)
    ans = 0
    for i in range(n+1):
        ans += c[s[i]-k]
        c[s[i]] -= 1
    print(ans)

if __name__ == '__main__':
    main()