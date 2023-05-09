def main():
    n = int(input())
    a = [0] * (n + 2)
    b = [0] * (n + 2)
    for i in range(1, n + 1):
        a[i], b[i] = map(int, input().split())
    s = [0] * (n + 2)
    for i in range(1, n + 1):
        s[a[i]] += 1
        s[a[i] + b[i]] -= 1
    for i in range(1, n + 1):
        s[i] += s[i - 1]
    for i in range(1, n + 1):
        print(s[i], end=' ')
    print()
