def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2 ** 30
    for i in range(N):
        or_value = 0
        xor_value = 0
        for j in range(i, N):
            or_value |= A[j]
            xor_value ^= A[j]
            if or_value == xor_value:
                ans = min(ans, or_value)
    print(ans)
