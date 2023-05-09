def main():
    N, M, Q = map(int, input().split())
    LR = []
    for i in range(M):
        LR.append(list(map(int, input().split())))
    PQ = []
    for i in range(Q):
        PQ.append(list(map(int, input().split())))
    LR = sorted(LR, key=lambda x: x[1])
    for p, q in PQ:
        count = 0
        for l, r in LR:
            if l >= p and r <= q:
                count += 1
        print(count)

if __name__ == '__main__':
    main()