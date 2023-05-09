def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (200001)
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(1, 200001):
        if B[i] == 0:
            continue
        for j in range(i, 200001, i):
            if j == i:
                ans += B[i] * (B[i] - 1) // 2
            else:
                ans += B[i] * B[j]
    print(ans)
main()
