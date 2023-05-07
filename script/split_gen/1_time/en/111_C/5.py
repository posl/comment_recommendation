def main():
    N = int(input())
    V = list(map(int, input().split()))
    A = V[0::2]
    B = V[1::2]
    import collections
    C = collections.Counter(A)
    D = collections.Counter(B)
    E = C.most_common()
    F = D.most_common()
    if E[0][0] == F[0][0]:
        if len(E) == 1 and len(F) == 1:
            print(N//2)
        elif len(E) == 1:
            print(N - F[0][1] - F[1][1])
        elif len(F) == 1:
            print(N - E[0][1] - E[1][1])
        else:
            print(N - max(E[0][1] + F[1][1], E[1][1] + F[0][1]))
    else:
        print(N - E[0][1] - F[0][1])
