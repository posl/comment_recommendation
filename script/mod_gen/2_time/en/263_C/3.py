def printSeq(N, M, seq):
    if N == 0:
        print(*seq)
    else:
        for i in range(1, M+1):
            if len(seq) == 0 or seq[-1] < i:
                printSeq(N-1, M, seq+[i])

if __name__ == '__main__':
    printSeq()