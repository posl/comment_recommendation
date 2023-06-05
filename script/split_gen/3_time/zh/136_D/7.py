def main():
    s = input()
    n = len(s)
    a = [0]*n
    for i in range(n):
        a[i] = 1
    for i in range(n):
        if s[i] == 'R':
            a[i+1] += a[i]
            a[i] = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            a[i-1] += a[i]
            a[i] = 0
    for i in range(n):
        print(a[i], end=' ')
    print()
