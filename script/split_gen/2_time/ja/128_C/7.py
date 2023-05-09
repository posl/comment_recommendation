def main():
    N, M = map(int, input().split())
    s = []
    p = []
    for _ in range(M):
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            tmp = 0
            for k in range(1, s[j][0]+1):
                if (i >> (s[j][k]-1)) & 1:
                    tmp += 1
            if tmp % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
