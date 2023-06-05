def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #result = [0]*(2*N+1)
    #print(result)
    #for i in range(2*N+1):
    #    print(i)
    #for i in range(2*N+1):
    #    print(A[i])
    #for i in range(2*N+1):
    #    print(result[i])
    #print('--------------------------')
    result = [0]*(2*N+1)
    #print(result)
    for i in range(N):
        #print(i)
        #print(A[i])
        result[A[i]] = 1
        #print(result)
        #print(result[2*i])
        #print(result[2*i+1])
        result[2*i] = result[A[i]] + 1
        result[2*i+1] = result[A[i]] + 1
        #print(result)
        #print(result[2*i])
        #print(result[2*i+1])
        #print('--------------------------')
    for i in range(1, 2*N+1):
        print(result[i])
