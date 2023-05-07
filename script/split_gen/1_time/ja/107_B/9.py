def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    # 行方向
    B = [list(map(lambda s: 1 if s == '.' else 0, a)) for a in A]
    for i in range(H):
        if sum(B[i]) == 0:
            B[i] = None
    B = list(filter(lambda b: b is not None, B))
    # 列方向
    C = [[b[i] for b in B] for i in range(len(B[0]))]
    for i in range(len(C)):
        if sum(C[i]) == 0:
            C[i] = None
    C = list(filter(lambda c: c is not None, C))
    # 行方向
    D = [[c[i] for c in C] for i in range(len(C[0]))]
    for d in D:
        print(''.join(list(map(lambda s: '.' if s == 1 else '#', d))))
