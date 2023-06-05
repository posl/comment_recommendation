def main():
    s = input()
    n = len(s)
    l = [0] * n
    r = [0] * n
    for i in range(1, n):
        if s[i] == 'L':
            l[i] = l[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if s[i] == 'R':
            r[i] = r[i + 1] + 1
    for i in range(n):
        print(l[i] + r[i] + 1, end=' ')
    print()
