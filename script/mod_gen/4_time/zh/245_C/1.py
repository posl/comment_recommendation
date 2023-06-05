def judge(N, K, A, B):
    A.sort()
    B.sort()
    B = B[::-1]
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            return False
    return True
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if __name__ == '__main__':
    judge()