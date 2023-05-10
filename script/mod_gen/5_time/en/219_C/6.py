def solve():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    D = dict()
    for i in range(26):
        D[X[i]] = chr(i+97)
    for i in range(N):
        S[i] = "".join([D[x] for x in S[i]])
    S.sort()
    for i in range(N):
        S[i] = "".join([X[ord(x)-97] for x in S[i]])
    print("\n".join(S))
solve()

if __name__ == '__main__':
    solve()