def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i]] = i + 1
    ans = 0
    for i in range(1, N + 1):
        if B[i] == i:
            ans += 1
        else:
            if B[B[i]] == i:
                ans += 1
    print(ans)
