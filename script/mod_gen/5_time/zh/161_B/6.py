def is_popular(A, M):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    for i in range(len(A)):
        if A[i] < sum / (4 * M):
            return False
    return True
N, M = input().split()
N = int(N)
M = int(M)
A = list(map(int, input().split()))
A.sort(reverse=True)

if __name__ == '__main__':
    is_popular()