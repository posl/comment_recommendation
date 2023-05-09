def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(10):
        min_cnt = 1000
        for j in range(N):
            cnt = 0
            for k in range(10):
                if S[j][k] == str(i):
                    cnt = k
                    break
            min_cnt = min(min_cnt, cnt)
        ans += min_cnt
    print(ans)
