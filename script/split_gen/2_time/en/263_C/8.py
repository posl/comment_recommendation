def main():
    n, m = map(int, input().split())
    s = [0] * n
    a = [0] * n
    for i in range(n):
        s[i] = i + 1
        a[i] = 1
    while True:
        print(' '.join(map(str, s)))
        i = n - 1
        while i >= 0 and s[i] == m - n + i + 1:
            i -= 1
        if i < 0:
            return
        s[i] += 1
        for j in range(i + 1, n):
            s[j] = s[j - 1] + 1
