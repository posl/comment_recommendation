def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        zero = 0
        one = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                one += 1
            else:
                zero += 1
        ans += zero * one * (2 ** i)
        ans %= 10 ** 9 + 7
    print(ans)
