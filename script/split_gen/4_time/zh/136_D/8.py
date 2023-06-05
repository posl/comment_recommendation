def main():
    s = input()
    n = len(s)
    ans = [0] * n
    r = 0
    l = 0
    for i in range(n):
        if s[i] == 'R':
            r = i
        else:
            l = i
        if s[i] == 'R' and s[i + 1] == 'L':
            ans[r] += (i + 1 - r) // 2
            ans[l] += (i + 1 - r + 1) // 2
            r = i + 1
    for i in range(n):
        print(ans[i], end=' ')
