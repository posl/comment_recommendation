def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N == K:
        if A[0] == A[-1]:
            print('Yes')
        else:
            print('No')
    else:
        if A[0] == A[K-1]:
            if A[-1] == A[K]:
                print('Yes')
            else:
                print('No')
        else:
            print('Yes')
