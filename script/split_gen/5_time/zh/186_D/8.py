def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    for i in range(n):
        s += a[i] * i - a[i] * (n - i - 1)
    print(s)
