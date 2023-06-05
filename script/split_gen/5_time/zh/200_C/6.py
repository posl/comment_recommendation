def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N,A)
    #print(A)
    #print(len(A))
    count = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            #print(i,j)
            if (A[i] - A[j]) % 200 == 0:
                count += 1
    print(count)
