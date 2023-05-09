def main():
    a, b, k = map(int, input().split())
    n = a + b
    c = 1
    for i in range(n):
        if a > 0:
            a -= 1
            c *= n - i
            c //= a + 1
        if c >= k:
            print('a', end='')
        else:
            print('b', end='')
            k -= c
