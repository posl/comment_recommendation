def solve():
    S = input()
    N = len(S)
    ans = [1] * N
    cnt = 0
    for i in range(N - 1):
        if S[i] == "R" and S[i + 1] == "L":
            cnt += 1
            ans[i] += cnt // 2
            ans[i + 1] += cnt // 2
            if cnt % 2:
                ans[i] += 1
            cnt = 0
        elif S[i] == "L" and S[i + 1] == "R":
            cnt = 1
        else:
            cnt += 1
    print(*ans)

if __name__ == '__main__':
    solve()