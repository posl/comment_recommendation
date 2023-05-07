def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            S[A - 1], S[B - 1] = S[B - 1], S[A - 1]
        else:
            S = S[N:] + S[:N]
    print("".join(S))
