def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l = 0
    r = k
    while l < r:
        m = (l + r) // 2
        if check(m, n, k, a, b):
            r = m
        else:
            l = m + 1
    print('Yes' if check(l, n, k, a, b) else 'No')
