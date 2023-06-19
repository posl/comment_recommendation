def solve():
    N, M = map(int, input().split())
    s = []
    for i in range(M):
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(1, s[j][0]+1):
                if i&(2**(s[j][k]-1)):
                    cnt += 1
            if cnt%2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
