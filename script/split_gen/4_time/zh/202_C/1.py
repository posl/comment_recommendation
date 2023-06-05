def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(B)
    #print(C)
    count = 0
    A.sort()
    B.sort()
    C.sort()
    #print(A)
    #print(B)
    #print(C)
    i = 0
    j = 0
    k = 0
    while i < N and j < N and k < N:
        if A[i] == B[C[j] - 1]:
            count += 1
            i += 1
            j += 1
        elif A[i] < B[C[j] - 1]:
            i += 1
        else:
            j += 1
    print(count)
