def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n+1):
        d[s[i]%m] += 1
    ans = 0
    for x in d.values():
        ans += x*(x-1)//2
    print(ans)

if __name__ == '__main__':
    main()