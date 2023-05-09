def main():
    # input
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs, Cs = [], []
    for _ in range(M):
        B, C = map(int, input().split())
        Bs.append(B)
        Cs.append(C)
    # compute
    As.sort(reverse=True)
    Cs.sort(reverse=True)
    for i in range(N):
        if i < M and As[i] < Cs[i]:
            As[i] = Cs[i]
        else:
            break
    # output
    print(sum(As))
