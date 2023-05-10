def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(n + 1):
        ans += d[s[i]]
        d[s[i] + k] += 1
    print(ans)

if __name__ == '__main__':
    main()