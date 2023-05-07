def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for i in range(M)]
    p = [0] * M
    for i in range(M):
        s[i] = list(map(int, input().split()))
        k[i] = s[i][0]
        s[i] = s[i][1:]
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = 1
        for j in range(M):
            count = 0
            for l in range(k[j]):
                if (i >> (s[j][l] - 1)) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = 0
                break
        if flag:
            ans += 1
    print(ans)
