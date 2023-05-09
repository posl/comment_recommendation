def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    s.sort()
    t.sort()
    i, j = 0, 0
    ans = 0
    while i < n and j < m:
        if s[i] < t[j]:
            i += 1
        elif s[i] > t[j]:
            j += 1
        else:
            ans += 1
            i += 1
            j += 1
    print(ans)

if __name__ == '__main__':
    main()