def main():
    import sys
    N = int(sys.stdin.readline())
    S = [sys.stdin.readline().rstrip() for _ in range(N)]
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
            S[i] += "({})".format(D[S[i]])
        else:
            D[S[i]] = 0
    print(*S, sep = "
")
