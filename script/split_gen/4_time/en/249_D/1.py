def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * 10**5 + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(1, 2 * 10**5 + 1):
        if B[i] == 0:
            continue
        for j in range(1, 2 * 10**5 // i + 1):
            if B[j] == 0:
                continue
            if i == j:
                ans += (B[i] * (B[i] - 1) * (B[i] - 2)) // 6
            elif i < j:
                ans += B[i] * B[j] * (B[i * j] - B[i] - B[j] + 1)
            else:
                ans += B[i] * B[j] * (B[i * j] - B[i] - B[j])
    print(ans)
