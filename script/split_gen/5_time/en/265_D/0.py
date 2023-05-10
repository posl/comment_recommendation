def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                for l in range(k+1, N):
                    if (A[i] + A[j] + A[k] == P) and (A[i] + A[j] + A[l] == Q) and (A[i] + A[k] + A[l] == R) and (A[j] + A[k] + A[l] == R):
                        ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')
