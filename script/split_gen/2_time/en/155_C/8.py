def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    S = S + [""]
    cnt = 1
    max_cnt = 0
    for i in range(N):
        if S[i] == S[i + 1]:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                ans = [S[i]]
            elif cnt == max_cnt:
                ans.append(S[i])
            cnt = 1
    for a in ans:
        print(a)
