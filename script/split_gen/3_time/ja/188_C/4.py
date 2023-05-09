def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [[i, A[i]] for i in range(len(A))]
    for i in range(N):
        for j in range(2**(N-i-1)):
            if A[2*j][1] > A[2*j+1][1]:
                A[2*j] = A[2*j+1]
    print(A[0][0]+1)
