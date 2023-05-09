def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    max = 0
    maxS = ""
    for i in range(N):
        if S[i] != maxS:
            maxS = S[i]
            max = 1
        else:
            max += 1
        if i == N-1:
            print(S[i])
        elif S[i+1] != maxS:
            print(S[i])

if __name__ == '__main__':
    solve()