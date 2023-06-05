def main():
    # n = int(input())
    # a = list(map(int, input().split()))
    n = 10
    a = [2, 2, 4, 1, 1, 1, 4, 2, 2, 1]
    p = 0
    for i in range(n):
        p += a[i] - 1
        p %= 4
    print(p)
