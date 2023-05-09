def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = 0
    for i in range(1, N + 1):
        ans += i * (N - i) * (N - i + 1) // 2
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if A[i] > A[j]:
                ans -= 1
    print(ans)
