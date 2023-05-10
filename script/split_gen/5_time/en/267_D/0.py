def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(1, N):
        A[i] += A[i-1]
    ans = 0
    for i in range(N):
        if i+M > N:
            break
        if i == 0:
            ans = max(ans, A[i+M-1])
        else:
            ans = max(ans, A[i+M-1]-A[i-1])
    print(ans)
