def check(N, K, A, B):
    for i in range(N):
        if abs(A[i]-B[i]) > K:
            return False
    return True
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if __name__ == '__main__':
    check()