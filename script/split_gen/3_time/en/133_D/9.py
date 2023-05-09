def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    #print(N)
    S = [0] * N
    S[0] = A[0]
    for i in range(1, N):
        S[i] = (A[i-1] - S[i-1]) // 2 + S[i-1]
    #print(S)
    T = [0] * N
    T[0] = S[0]
    for i in range(1, N):
        T[i] = (A[i-1] - T[i-1]) // 2 + S[i]
    #print(T)
    for i in range(N):
        print(T[i] * 2, end = " ")
    print()
main()
