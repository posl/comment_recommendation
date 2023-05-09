def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (N-1-i)*A[i] - i*A[i]
    print(ans)
