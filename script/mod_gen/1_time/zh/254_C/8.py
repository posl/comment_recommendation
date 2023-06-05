def sort_check(N, K, A):
    for i in range(N - K):
        if A[i] > A[i + K]:
            return False
    return True
N, K = map(int, input().split())
A = list(map(int, input().split()))

if __name__ == '__main__':
    sort_check()