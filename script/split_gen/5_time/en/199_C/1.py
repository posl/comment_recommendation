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
    # FLIP
    first = S[:N]
    last = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N and B[i] <= N:
                first = first[:A[i]-1] + last[B[i]-1] + first[A[i]:]
                last = last[:B[i]-1] + first[A[i]-1] + last[B[i]:]
            elif A[i] > N and B[i] > N:
                first = first[:A[i]-1-N] + last[B[i]-1-N] + first[A[i]-N:]
                last = last[:B[i]-1-N] + first[A[i]-1-N] + last[B[i]-N:]
            else:
                first = last[:B[i]-1-N] + first[A[i]-1] + last[B[i]-N:]
                last = first[:A[i]-1] + last[B[i]-1] + first[A[i]:]
        elif T[i] == 2:
            first, last = last, first
    print(first + last)
