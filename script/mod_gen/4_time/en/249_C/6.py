def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(2**n):
        cnt = 0
        for j in range(n):
            if (i >> j) & 1:
                cnt += 1
        if cnt != k:
            continue
        a = []
        for j in range(n):
            if (i >> j) & 1:
                a.append(s[j])
        a = ''.join(a)
        cnt = 0
        for j in range(26):
            if a.count(chr(ord('a')+j)) > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()