def main():
    #input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #compute
    A.sort(reverse=True)
    B.sort()
    #output
    for i in range(K):
        if A[i] == A[i+1]:
            continue
        if i+1 == B[i]:
            print('Yes')
            return
    print('No')
