def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    ans = []
    cnt = 1
    max_cnt = 1
    for i in range(1, N):
        if S[i] == S[i - 1]:
            cnt += 1
        else:
            if cnt > max_cnt:
                ans = [S[i - 1]]
                max_cnt = cnt
            elif cnt == max_cnt:
                ans.append(S[i - 1])
            cnt = 1
    if cnt > max_cnt:
        ans = [S[N - 1]]
    elif cnt == max_cnt:
        ans.append(S[N - 1])
    ans.sort()
    for s in ans:
        print(s)
