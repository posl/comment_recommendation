def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * 10 ** 5 + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(1, 2 * 10 ** 5 + 1):
        if B[i] == 0:
            continue
        for j in range(i, 2 * 10 ** 5 + 1, i):
            if B[j] == 0:
                continue
            if i == j:
                ans += B[i] * (B[i] - 1) // 2
            else:
                ans += B[i] * B[j]
    print(ans)
