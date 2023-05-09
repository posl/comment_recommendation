def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    #print(2**N)
    for i in range(N):
        #print("i=",i)
        for j in range(1,2**(N-i),2):
            #print("j=",j)
            #print("A[{}]={}".format(j-1,A[j-1]))
            #print("A[{}]={}".format(j,A[j]))
            if A[j-1] > A[j]:
                A[j-1] = 0
            else:
                A[j] = 0
    #print(A)
    for i in range(len(A)):
        if A[i] != 0:
            print(i+1)
