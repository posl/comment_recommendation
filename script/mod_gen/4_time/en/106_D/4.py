def main():
    N, M, Q = map(int, input().split())
    LR = []
    for i in range(M):
        LR.append(list(map(int, input().split())))
    PQ = []
    for i in range(Q):
        PQ.append(list(map(int, input().split())))
    for i in range(Q):
        count = 0
        for j in range(M):
            if LR[j][0] >= PQ[i][0] and LR[j][1] <= PQ[i][1]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()