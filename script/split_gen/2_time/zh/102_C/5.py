def main():
    N = int(input())
    A = list(map(int, input().split()))
    b = 0
    for i in range(N):
        b += A[i] - (i+1)
    b //= N
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b + i + 1))
    print(ans)
