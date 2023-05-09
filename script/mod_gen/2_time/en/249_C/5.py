def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1, 2 ** n):
        b = bin(i)[2:].zfill(n)
        tmp = set()
        for j in range(n):
            if b[j] == '1':
                for c in s[j]:
                    tmp.add(c)
        if len(tmp) == k:
            ans = max(ans, len(tmp))
    print(ans)

if __name__ == '__main__':
    main()