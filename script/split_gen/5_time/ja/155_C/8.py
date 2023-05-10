def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    cnt = 1
    ans = []
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            if cnt == max_cnt:
                ans.append(S[i])
            elif cnt > max_cnt:
                ans = [S[i]]
                max_cnt = cnt
            cnt = 1
    if cnt == max_cnt:
        ans.append(S[-1])
    elif cnt > max_cnt:
        ans = [S[-1]]
    ans.sort()
    for i in ans:
        print(i)
