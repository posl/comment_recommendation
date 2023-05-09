def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if N == K:
        print('Yes')
    else:
        A.sort()
        if A[-1] <= A[N-K-1]:
            print('No')
        else:
            print('Yes')
main()
