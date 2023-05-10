def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        tmp = set()
        for j in range(n):
            if i & (1 << j):
                tmp |= set(s[j])
        if len(tmp) == k:
            ans = max(ans, bin(i).count('1'))
    print(ans)

if __name__ == '__main__':
    main()