def makeSeqs(N, M, i, seq):
    if i == N:
        print(*seq)
        return
    for j in range(1, M+1):
        if i == 0 or seq[i-1] < j:
            seq[i] = j
            makeSeqs(N, M, i+1, seq)
N, M = map(int, input().split())
makeSeqs(N, M, 0, [0]*N)
