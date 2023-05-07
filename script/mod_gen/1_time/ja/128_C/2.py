def main():
    N, M = map(int, input().split())
    k = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for l in k[j][1:]:
                if i & (1 << (l - 1)):
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()