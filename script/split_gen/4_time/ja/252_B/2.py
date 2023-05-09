def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max = 0
    for i in range(N):
        if max < A[i]:
            max = A[i]
    for i in range(K):
        if max == B[i]:
            print('Yes')
            exit()
    print('No')
