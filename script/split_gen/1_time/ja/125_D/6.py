def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = sum(A)
    for i in range(1, N-1):
        if A[i-1] < 0 and A[i] < 0 and A[i+1] < 0:
            ans -= min(A[i-1], A[i], A[i+1])
        elif A[i-1] > 0 and A[i] > 0 and A[i+1] > 0:
            ans -= min(A[i-1], A[i], A[i+1])
    print(ans)
