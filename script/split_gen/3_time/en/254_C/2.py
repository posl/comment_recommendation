def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if N == 1:
        print('Yes')
        return
    if N == 2:
        if A[0] == A[1]:
            print('Yes')
        else:
            print('No')
        return
    if K == 1:
        for i in range(1, N):
            if A[i-1] == A[i]:
                print('Yes')
                return
        print('No')
        return
    if K == 2:
        for i in range(1, N-1):
            if A[i-1] == A[i] or A[i] == A[i+1] or A[i-1] == A[i+1]:
                print('Yes')
                return
        print('No')
        return
    if K >= 3:
        print('Yes')
        return
