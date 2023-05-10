def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if A[i]+A[i+1] < 0:
            ans += 2*min(A[i], A[i+1])
            A[i] = 0
            A[i+1] = 0
    print(ans + sum(A))
