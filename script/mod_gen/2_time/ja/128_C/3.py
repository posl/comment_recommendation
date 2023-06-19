def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for i in range(M)]
    p = [0] * M
    for i in range(M):
        line = list(map(int, input().split()))
        k[i] = line[0]
        for j in range(k[i]):
            s[i][line[j+1]-1] = 1
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        tmp = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M):
                    tmp[k] += s[k][j]
        flag = True
        for j in range(M):
            if tmp[j] % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
main()
