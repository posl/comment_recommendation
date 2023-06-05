def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    #print(A)
    #print(N)
    #print(A[N-1])
    #print(A[N-2])
    #print(A[N-3])
    #print(A[N-4])
    #print(A[N-5])
    count = 0
    for i in range(N-1):
        if A[i] != A[i+1]:
            count += 1
    if A[N-1] != A[N-2]:
        count += 1
    print(count)
