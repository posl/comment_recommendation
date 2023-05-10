def main():
    n, a, b = map(int, input().split())
    s = input()
    c = 0
    d = 0
    for i in range(n):
        if s[i] != s[n - i - 1]:
            c += 1
        elif s[i] == s[n - i - 1] and i < n // 2:
            d += 1
    if c == 0:
        print(0)
    elif c == 1:
        print(a)
    elif c == 2:
        print(min(a, b))
    else:
        if a > b:
            print(b * (c - 1) + a)
        else:
            print(b * c)
