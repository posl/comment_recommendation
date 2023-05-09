def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    for i in range(n):
        if i % 2 == 0:
            a[0] += s[i]
        else:
            a[0] -= s[i]
    a[0] = a[0] // 2
    for i in range(1, n):
        a[i] = s[i - 1] - a[i - 1]
    print(*a)
