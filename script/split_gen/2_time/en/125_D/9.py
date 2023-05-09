def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    if N%2==0:
        print(sum(A[0:N//2]))
    else:
        print(sum(A[0:N//2+1]))
