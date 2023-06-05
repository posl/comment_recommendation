def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    #print('N = ',N)
    #print('A = ',A)
    #print('B = ',B)
    sum = 0
    for i in range(N):
        if A[i] <= B[i]:
            sum += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            sum += B[i]
            A[i] -= B[i]
            B[i] = 0
        if A[i+1] <= B[i]:
            sum += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            sum += B[i]
            A[i+1] -= B[i]
            B[i] = 0
    print(sum)
