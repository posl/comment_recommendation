def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    LR.sort(key=lambda x: x[0])
    for pq in PQ:
        print(sum(1 for lr in LR if pq[0] <= lr[0] and lr[1] <= pq[1]))

if __name__ == '__main__':
    main()