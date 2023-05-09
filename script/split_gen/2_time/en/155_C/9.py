def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    S.append('') #dummy
    cnt = 1
    max_cnt = 0
    ans = []
    for i in range(N):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            if cnt > max_cnt:
                ans = [S[i]]
                max_cnt = cnt
            elif cnt == max_cnt:
                ans.append(S[i])
            cnt = 1
    for s in ans:
        print(s)
