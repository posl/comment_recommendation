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
    is_reverse = False
    for i in range(Q):
        if T[i] == 1:
            if is_reverse:
                a = A[i] + N if A[i] <= N else A[i] - N
                b = B[i] + N if B[i] <= N else B[i] - N
                S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
            else:
                S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            is_reverse = not is_reverse
    if is_reverse:
        S = S[N:] + S[:N]
    print(S)
