def solve():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if S == S[::-1]:
        print(ans)
        return
    if N % 2 == 0:
        for i in range(N//2):
            if S[i] != S[N-1-i]:
                ans += min(A, B)
        print(ans)
        return
    else:
        for i in range(N//2):
            if S[i] != S[N-1-i]:
                ans += min(A, B)
        for i in range(N//2+1):
            if S[i] != S[N-1-i]:
                ans += min(A, B)
                print(ans)
                return
        print(ans)
        return
solve()

if __name__ == '__main__':
    solve()