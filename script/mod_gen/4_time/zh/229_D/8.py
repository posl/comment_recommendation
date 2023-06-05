def solve(S,K):
    # S = list(S)
    S = S.replace('.','0')
    S = S.replace('X','1')
    S = list(S)
    # print(S)
    if K == 0:
        ans = 0
        cnt = 0
        for i in range(len(S)):
            if S[i] == '1':
                cnt += 1
            else:
                ans = max(ans,cnt)
                cnt = 0
        ans = max(ans,cnt)
        return ans
    else:
        ans = 0
        cnt = 0
        for i in range(len(S)):
            if S[i] == '1':
                cnt += 1
            else:
                if K > 0:
                    K -= 1
                    cnt += 1
                else:
                    ans = max(ans,cnt)
                    cnt = 0
        ans = max(ans,cnt)
        return ans

if __name__ == '__main__':
    solve()