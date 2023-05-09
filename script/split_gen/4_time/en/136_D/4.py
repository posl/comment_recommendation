def main():
    s = input()
    l = len(s)
    ans = [0] * l
    r = 0
    l = 0
    for i in range(len(s)):
        if s[i] == 'R':
            r += 1
        else:
            l += 1
            ans[i] += l // 2
            ans[i - 1] += l - l // 2
            l = 0
    l = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'L':
            l += 1
        else:
            ans[i] += l // 2
            ans[i + 1] += l - l // 2
            l = 0
    print(' '.join(map(str, ans)))
