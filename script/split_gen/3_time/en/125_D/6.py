def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * N
    for i in range(N):
        B[i] = abs(A[i])
    #print(B)
    if sum(A) < 0:
        for i in range(N):
            if A[i] > 0:
                A[i] = -A[i]
    #print(A)
    if sum(A) < 0:
        for i in range(N):
            if A[i] == 0:
                A[i] = 1
    #print(A)
    if sum(A) < 0:
        for i in range(N):
            if A[i] < 0:
                A[i] = -A[i]
    #print(A)
    print(sum(A))
