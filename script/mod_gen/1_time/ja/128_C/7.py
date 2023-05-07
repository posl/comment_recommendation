def main():
    N, M = map(int, input().split())
    s = [[int(x) for x in input().split()] for _ in range(M)]
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(1, s[j][0]+1):
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