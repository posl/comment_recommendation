def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N-K):
        if A[i] < A[i+K]:
            print('Yes')
        else:
            print('No')
