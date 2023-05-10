def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    sum_A = sum(A)
    for i in range(N):
        sum_A -= A[i]
        ans += A[i] * sum_A
    print(ans % (10**9 + 7))
