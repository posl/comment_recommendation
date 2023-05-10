def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if P == A[i] + A[i-1] and Q == A[j] + A[j-1] and R == A[k] + A[k-1]:
                    ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')
