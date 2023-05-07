def main():
    N = int(input())
    S = input()
    Q = int(input())
    S1 = S[:N]
    S2 = S[N:]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            if A <= N and B <= N:
                S1 = swap(S1, A-1, B-1)
            elif A > N and B > N:
                S2 = swap(S2, A-1-N, B-1-N)
            else:
                S1 = swap(S1, A-1, B-1-N)
                S2 = swap(S2, A-1-N, B-1)
        else:
            S1, S2 = S2, S1
    print(S1+S2)
