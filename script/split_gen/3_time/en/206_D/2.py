def main():
    N = int(input())
    A = list(map(int,input().split()))
    if N==1:
        print(0)
        return
    if N==2:
        if A[0]==A[1]:
            print(0)
        else:
            print(1)
        return
    #print(A)
    #print(N)
    A = [0]+A+[0]
    #print(A)
    #print(N)
    A2 = []
    for i in range(1,N+1):
        A2.append(A[i])
        if A[i]==A[i+1]:
            A2.append(0)
    #print(A2)
    #print(len(A2))
    A = A2
    N = len(A)
    A = [0]+A+[0]
    #print(A)
    #print(N)
    #print(A)
    #print(N)
    #print(A)
    #print(N)
    A2 = []
    for i in range(1,N+1):
        A2.append(A[i])
        if A[i]==A[i+1]:
            A2.append(0)
    #print(A2)
    #print(len(A2))
    A = A2
    N = len(A)
    A = [0]+A+[0]
    #print(A)
    #print(N)
    #print(A)
    #print(N)
    #print(A)
    #print(N)
    A2 = []
    for i in range(1,N+1):
        A2.append(A[i])
        if A[i]==A[i+1]:
            A2.append(0)
    #print(A2)
    #print(len(A2))
    A = A2
    N = len(A)
    A = [0]+A+[0]
    #print(A)
    #print(N)
    #print(A)
    #print(N)
    #print(A)
    #print(N)
    A2 = []
    for i in range(1,N+1):
        A2.append(A[i])
        if A[i]==A[i+1]:
            A2.append(0)
    #print(A2)
    #print(len(A2))
    A = A2
    N = len(A)
    A = [0]+A+[0]
    #print(A)
    #print(N)
    #print(A)
