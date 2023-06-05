def solve():
    S = input()
    N = len(S)
    cnt = 0
    for i in range(N):
        if S[i] == '1':
            cnt += 1
    print(min(cnt, N-cnt)*2)
