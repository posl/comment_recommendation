def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    #print(N)
    #print(A)
    #print(B)
    #print(C)
    cnt = 0
    for i in range(1, N+1):
        cnt += B[C[i-1]-1] == A[i-1]
    print(cnt)
