def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    #print(A)
    #print(N)
    #print(len(A))
    #print(len(A)//2)
    for i in range(1, N+1):
        for j in range(1, len(A)//2):
            if A[2*j-1] > A[2*j]:
                A[2*j-1] = 0
            else:
                A[2*j] = 0
    #print(A)
    for i in range(len(A)):
        if A[i] != 0:
            print(i)
            break
