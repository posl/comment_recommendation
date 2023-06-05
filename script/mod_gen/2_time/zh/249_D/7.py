def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count('1') != k:
            continue
        c = set()
        for j in range(n):
            if i >> j & 1:
                c |= set(s[j])
        if len(c) == k:
            ans = max(ans, bin(i).count('1'))
    print(ans)

if __name__ == '__main__':
    main()