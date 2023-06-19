def solve():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1,N):
        if S[i-1] != S[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()