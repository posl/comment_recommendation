def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    ans = 0
    for i in range(n):
        ans += abs(b[i] - b[n // 2])
    print(ans)
