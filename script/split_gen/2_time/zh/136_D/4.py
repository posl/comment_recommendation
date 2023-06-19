def main():
    s = input()
    n = len(s)
    ans = [0] * n
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            l = i
        else:
            r = i
        if s[i] == 'R':
            ans[r] += 1
        else:
            ans[l] += 1
    print(' '.join(map(str, ans)))
