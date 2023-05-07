def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += max(a[i] - k * x, 0)
    print(s)
