def solve():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 1
    for i in range(N):
        if S[i] == 'OR':
            ans += 2**(i+1)
    print(ans)
