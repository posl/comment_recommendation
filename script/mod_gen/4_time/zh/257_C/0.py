def solve():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i] != S[i - 1]:
            ans += 1
    if ans == 0:
        if S[0] == '0':
            print(0)
        else:
            print(N)
    else:
        print(min(ans + 2, N))

if __name__ == '__main__':
    solve()