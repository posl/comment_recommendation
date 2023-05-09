def solve():
    N = int(input())
    S = input()
    ans = []
    for i in range(1,N):
        l = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                l += 1
            else:
                break
        ans.append(l)
    print(*ans, sep='
')
