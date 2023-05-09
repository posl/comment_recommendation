def main():
    N = int(input())
    A = list(map(int, input().split()))
    #N = 4
    #A = [6, 13, 12, 5, 3, 7, 10, 11, 16, 9, 8, 15, 2, 1, 14, 4]
    #print(A)
    #print(N)
    P = [0] * (2**N)
    for i in range(2**N):
        P[i] = i+1
    #print(P)
    for i in range(N):
        for j in range(2**(N-i-1)):
            if A[P[2*j]-1] > A[P[2*j+1]-1]:
                P[j] = P[2*j]
            else:
                P[j] = P[2*j+1]
    print(P[0])
