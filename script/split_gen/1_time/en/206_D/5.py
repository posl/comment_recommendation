def main():
    n = int(input())
    a = list(map(int, input().split()))
    print((n - 1) // 2 - sum(a[::2]) + sum(a[1::2]))
