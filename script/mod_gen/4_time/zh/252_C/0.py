def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ans = 10 ** 9
    for i in range(n):
        for j in range(10):
            cnt = 0
            for k in range(n):
                if s[k][(j + k) % 10] != s[i][(j + i) % 10]:
                    cnt += 1
            ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()