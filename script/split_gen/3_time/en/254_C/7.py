def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [A[i] - (i+1) for i in range(N)]
    A.sort()
    B = A[:]
    for i in range(N):
        B[i] -= i
    if B[0] == B[N-1]:
        print('Yes')
    elif K == 1:
        print('No')
    else:
        if B[0] % K == B[N-1] % K:
            print('Yes')
        else:
            print('No')
