def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    #print()
    #N, M, Q = 2, 3, 1
    #LR = [[1, 1], [1, 2], [2, 2]]
    #PQ = [[1, 2]]
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    #print()
    LR.sort()
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    #print()
    for i in range(Q):
        #print(PQ[i])
        #print()
        #print(LR)
        #print(PQ[i])
        #print()
        #print(LR[0][0])
        #print(PQ[i][0])
        #print()
        #print(LR[0][1])
        #print(PQ[i][1])
        #print()
        #print()
        #print()
        print(sum([1 for j in range(M) if LR[j][0] <= PQ[i][0] and LR[j][1] >= PQ[i][1]]))

if __name__ == '__main__':
    main()