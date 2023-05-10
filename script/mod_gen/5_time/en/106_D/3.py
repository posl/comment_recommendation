def main():
    N, M, Q = map(int, input().split())
    LR = []
    for _ in range(M):
        LR.append(list(map(int, input().split())))
    pq = []
    for _ in range(Q):
        pq.append(list(map(int, input().split())))
    LR.sort(key=lambda x: x[1])
    for p, q in pq:
        count = 0
        for l, r in LR:
            if p <= l and r <= q:
                count += 1
        print(count)

if __name__ == '__main__':
    main()