def main():
    N, M = map(int, input().split())
    s = [0] * M
    p = [0] * M
    for i in range(M):
        s[i] = list(map(int, input().split()))
        s[i].pop(0)
    p = list(map(int, input().split()))
    ans = 0
    for bit in range(2 ** N):
        flag = True
        for i in range(M):
            cnt = 0
            for j in range(len(s[i])):
                if (bit >> (s[i][j] - 1)) & 1:
                    cnt += 1
            if cnt % 2 != p[i]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
