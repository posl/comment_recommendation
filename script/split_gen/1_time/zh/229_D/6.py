def main():
    s = input()
    k = int(input())
    n = len(s)
    a = [0] * n
    for i in range(n):
        if s[i] == 'X':
            a[i] = 1
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
    for i in range(n):
        if s[i] == '.':
            ans = max(ans, b[min(i + k + 1, n)] - b[max(i - k, 0)])
    print(ans)
