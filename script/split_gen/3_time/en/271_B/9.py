def main():
    # Read input
    N, Q = map(int, input().split())
    L = [0] * N
    A = [0] * N
    for i in range(N):
        L[i] = int(input().split()[0])
        A[i] = list(map(int, input().split()))
    S = [0] * Q
    T = [0] * Q
    for i in range(Q):
        S[i], T[i] = map(int, input().split())
    
    # Solve
    # Calculate the number of elements before each sequence
    B = [0] * N
    B[0] = 0
    for i in range(1, N):
        B[i] = B[i-1] + L[i-1]
    
    # Output
    for i in range(Q):
        print(A[S[i]-1][T[i]-1])
