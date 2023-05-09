def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[A[i]] = i
    ans = 0
    for i in range(1, N + 1):
        if B[i] == i:
            if i + 1 <= N and B[i + 1] == i + 1:
                ans += 1
        else:
            if i < B[i] and B[i] < B[i + 1]:
                ans += 1
    print(ans)
