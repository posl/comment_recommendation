def main():
    N = int(input())
    a = [0] * 10
    b = [0] * 10
    for i in range(1, N + 1):
        a[i % 10] += 1
        b[i // 10 % 10] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += a[i] * b[j] * (i == j)
    print(ans)
