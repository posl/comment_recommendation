def main():
    N,K,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #print(N,K,X)
    #print(A)
    #print(A[0])
    sum = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                sum += A[i] - X
                K -= 1
            else:
                sum += A[i]
        else:
            sum += A[i]
    print(sum)
