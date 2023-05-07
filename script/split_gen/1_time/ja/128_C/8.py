def main():
    N, M = map(int, input().split())
    s = []
    p = []
    for i in range(M):
        s.append(list(map(int, input().split())))
        s[i].pop(0)
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in s[j]:
                if ((i >> (k - 1)) & 1) == 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
