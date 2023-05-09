def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    s = sum(a)
    k = x // s
    r = x % s
    i = 0
    while r >= 0:
        r -= a[i]
        i += 1
    print(k * n + i)
