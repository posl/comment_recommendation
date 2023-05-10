def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    for p, q in PQ:
        print(sum(1 for l, r in LR if p <= l <= r <= q))
