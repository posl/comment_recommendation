def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(K):
        if A[B[i]-1] == max(A):
            print('Yes')
            return
    print('No')
