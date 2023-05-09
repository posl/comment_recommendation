def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    if N == 1:
        print(0)
        return
    if N % 2 == 0:
        #print("N is even")
        #print(A[0:N//2])
        #print(A[N//2:])
        #print(A[0:N//2])
        #print(A[N//2:])
        if A[0:N//2] == A[N//2:]:
            print(0)
            return
        else:
            print(1)
            return
    else:
        #print("N is odd")
        #print(A[0:N//2])
        #print(A[N//2+1:])
        if A[0:N//2] == A[N//2+1:]:
            print(0)
            return
        else:
            print(1)
            return
