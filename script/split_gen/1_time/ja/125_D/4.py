def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = a[i] + b[i - 1]
    ans = 0
    for i in range(1, n + 1):
        if b[i] > 0:
            ans += b[i]
    print(ans)
