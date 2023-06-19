def count(L,R,X):
    count = 0
    for i in range(L-1,R):
        if A[i] == X:
            count += 1
    return count
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
for i in range(Q):
    L,R,X = map(int,input().split())
    print(count(L,R,X))
