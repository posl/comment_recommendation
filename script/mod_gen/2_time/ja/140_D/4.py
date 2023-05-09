def solve():
    N, K = map(int, input().split())
    S = input()
    S = S.replace("R", "1").replace("L", "0")
    S = S.replace("1", "R").replace("0", "L")
    ans = 0
    for i in range(N):
        if S[i] == "R":
            r = i
            for j in range(i, N):
                if S[j] == "L":
                    l = j
                    break
            else:
                l = N
            ans += min(r - i + l - r, K) * 2 + 1
            i = l
    print(ans)

if __name__ == '__main__':
    solve()