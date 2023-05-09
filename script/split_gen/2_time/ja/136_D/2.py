def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[N-1] = 1
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L':
            cnt = 1
            for j in range(i+1,N):
                if S[j] == 'L':
                    cnt += 1
                else:
                    break
            if cnt % 2 == 1:
                ans[i] += cnt // 2 + 1
                ans[i+1] += cnt // 2
            else:
                ans[i] += cnt // 2
                ans[i+1] += cnt // 2
        elif S[i] == 'L' and S[i+1] == 'R':
            cnt = 1
            for j in range(i-1,-1,-1):
                if S[j] == 'R':
                    cnt += 1
                else:
                    break
            if cnt % 2 == 1:
                ans[i] += cnt // 2 + 1
                ans[i+1] += cnt // 2
            else:
                ans[i] += cnt // 2
                ans[i+1] += cnt // 2
    print(*ans)
