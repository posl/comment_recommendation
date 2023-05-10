def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    is_front = True
    for i in range(Q):
        if T[i] == 1:
            if is_front:
                S = S[:A[i] - 1] + S[B[i] - 1] + S[A[i]:B[i] - 1] + S[A[i] - 1] + S[B[i]:]
            else:
                if A[i] <= N:
                    A[i] = A[i] + N
                else:
                    A[i] = A[i] - N
                if B[i] <= N:
                    B[i] = B[i] + N
                else:
                    B[i] = B[i] - N
                S = S[:A[i] - 1] + S[B[i] - 1] + S[A[i]:B[i] - 1] + S[A[i] - 1] + S[B[i]:]
        else:
            is_front = not is_front
    if not is_front:
        S = S[N:] + S[:N]
    print(S)
