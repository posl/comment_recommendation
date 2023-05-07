def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    
    S1 = S[:N]
    S2 = S[N:]
    
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                if B[i] <= N:
                    S1 = S1[:A[i]-1] + S1[B[i]-1] + S1[A[i]:B[i]-1] + S1[A[i]-1] + S1[B[i]:]
                else:
                    S1 = S1[:A[i]-1] + S2[B[i]-N-1] + S1[A[i]:B[i]-N-1] + S1[A[i]-1] + S1[B[i]-N:]
                    S2 = S2[:B[i]-N-1] + S1[A[i]-1] + S2[A[i]:B[i]-N-1] + S2[B[i]-N-1] + S2[B[i]-N:]
            else:
                if B[i] <= N:
                    S2 = S2[:A[i]-N-1] + S1[B[i]-1] + S2[A[i]-N:B[i]-1] + S2[A[i]-N-1] + S2[B[i]:]
                    S1 = S1[:B[i]-1] + S2[A[i]-N-1] + S1[A[i]:B[i]-1] + S1[B[i]-1] + S1[B[i]:]
                else:
                    S2 = S2[:A[i]-N-1] + S2[B[i]-N-1] + S2[A[i]-N:B[i]-N-1] + S2[A[i]-N-1] + S2[B[i]-N:]
        else:
            S1, S2 = S2, S1
    
    print(S1 + S2)
