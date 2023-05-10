def main():
    N, M = map(int, raw_input().split())
    A = [0] * N
    def rec(i, m):
        if i == N:
            print " ".join(map(str, A))
            return
        for j in xrange(m, M + 1):
            A[i] = j
            rec(i + 1, j + 1)
    rec(0, 1)
main()
