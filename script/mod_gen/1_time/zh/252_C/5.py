def solve():
    #input
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #init
    ans = 0
    #solve
    for i in range(10):
        for j in range(N):
            if S[j][i] != str(i):
                ans += 1
                break
    #output
    print(ans)
    return 0

if __name__ == '__main__':
    solve()