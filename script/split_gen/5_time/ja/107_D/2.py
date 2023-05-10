def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - i - 1
    B.sort()
    med = B[N // 2]
    ans = 0
    for i in range(N):
        ans += abs(B[i] - med)
    print(ans)
