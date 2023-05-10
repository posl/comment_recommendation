def solve():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    cnt = 0
    prev = '0'
    for i in range(N):
        if S[i] == '0':
            if prev == '1':
                cnt += 1
            else:
                cnt = 1
        else:
            cnt += 1
        if cnt > ans:
            ans = cnt
        prev = S[i]
    if K > 0:
        cnt = 0
        prev = '1'
        for i in range(N):
            if S[i] == '0':
                if prev == '1':
                    cnt += 1
                else:
                    cnt = 1
            else:
                cnt += 1
            if cnt > ans:
                ans = cnt
            prev = S[i]
    if ans > N:
        ans = N
    print(ans)

if __name__ == '__main__':
    solve()