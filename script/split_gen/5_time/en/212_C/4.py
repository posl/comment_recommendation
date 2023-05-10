def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    j = 0
    for i in range(N):
        while j < M-1 and abs(A[i]-B[j]) >= abs(A[i]-B[j+1]):
            j += 1
        ans = min(ans, abs(A[i]-B[j]))
    print(ans)
