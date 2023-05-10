def main():
    n, m = map(int, input().split())
    s = []
    p = []
    for i in range(m):
        s.append(list(map(int, input().split()))[1:])
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(m):
            cnt = 0
            for k in range(len(s[j])):
                if (i >> (s[j][k]-1)) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()