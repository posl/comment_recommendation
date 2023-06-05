def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    for i in range(1, 2 * n + 1):
        j = i
        cnt = 0
        while j > 0:
            j //= 2
            cnt += 1
        print(cnt - 1 + b[i])
