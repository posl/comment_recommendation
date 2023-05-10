def main():
    n, m = map(int, input().split())
    s = []
    p = []
    for _ in range(m):
        *si, pi = map(int, input().split())
        s.append(si)
        p.append(pi)
    ans = 0
    for i in range(1 << n):
        flag = True
        for j in range(m):
            cnt = 0
            for k in s[j]:
                if i & (1 << (k - 1)):
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()