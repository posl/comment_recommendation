def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for i in range(M)]
    p = [0] * M
    for i in range(M):
        input_list = list(map(int, input().split()))
        k[i] = input_list[0]
        for j in range(1, k[i] + 1):
            s[i][input_list[j] - 1] = 1
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        tmp = 0
        for j in range(M):
            cnt = 0
            for l in range(N):
                if s[j][l] == 1 and (i >> l & 1):
                    cnt += 1
            if cnt % 2 == p[j]:
                tmp += 1
        if tmp == M:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()