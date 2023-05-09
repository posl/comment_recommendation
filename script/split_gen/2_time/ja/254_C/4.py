def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if K == 1:
        if len(set(A)) == N:
            print('Yes')
        else:
            print('No')
    else:
        if A[N-1] - A[0] <= K:
            print('Yes')
        else:
            print('No')
    return
