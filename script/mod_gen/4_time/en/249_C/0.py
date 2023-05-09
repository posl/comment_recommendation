def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << 26):
        cnt = 0
        for j in range(n):
            c = 0
            for l in range(26):
                if (i >> l) & 1:
                    if chr(97 + l) in s[j]:
                        c += 1
            if c >= k:
                cnt += 1
        if cnt == n:
            ans = max(ans, bin(i).count('1'))
    print(ans)

if __name__ == '__main__':
    main()