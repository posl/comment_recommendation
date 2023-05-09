def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0]*Q
    A = [0]*Q
    B = [0]*Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                if B[i] <= N:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
                else:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:N] + S[A[i]-1] + S[N:B[i]-1] + S[B[i]:]
            else:
                if B[i] <= N:
                    S = S[:N] + S[A[i]-1] + S[N:B[i]-1] + S[A[i]:N] + S[B[i]:]
                else:
                    S = S[:N] + S[A[i]-1] + S[N:B[i]-1] + S[A[i]:N] + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)
