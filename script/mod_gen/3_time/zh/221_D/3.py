def solve():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(len(A))
    #print(len(B))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    C = [0]*N
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i] <= A[j] and A[j] < A[i]+B[i]:
                    C[i] += 1
    print(C)
    for i in range(N):
        print(C[i],

if __name__ == '__main__':
    solve()