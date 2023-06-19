def solve():
    N = int(input())
    S = input()
    cnt = 0
    w_cnt = 0
    for i in range(N):
        if S[i] == 'W':
            w_cnt += 1
        else:
            cnt += w_cnt
    print(cnt)
solve()
