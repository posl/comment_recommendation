def count(K, A):
    A.sort()
    count = 0
    for i in range(len(A)):
        if A[i] > A[K]:
            count += 1
    return count
N = int(input())
A = [int(i) for i in input().split()]
for i in range(N):
    print(count(i, A))
