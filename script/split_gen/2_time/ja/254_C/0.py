def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    for i in range(N-K):
        if A[i] > A[i+K]:
            print('No')
            return
    print('Yes')
