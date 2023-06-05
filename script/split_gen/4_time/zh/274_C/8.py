def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2*n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    for i in range(1, 2*n + 1):
        j = i
        while j > 0 and b[j] < b[(j + 1) // 2]:
            b[j], b[(j + 1) // 2] = b[(j + 1) // 2], b[j]
            j = (j + 1) // 2
    for i in range(1, 2*n + 1):
        j = i
        ans = 0
        while j > 1:
            j //= 2
            ans += 1
        print(ans)
