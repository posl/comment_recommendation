def main():
    s = input()
    n = len(s)
    ans = [0]*n
    pos = 0
    while pos < n:
        if s[pos] == 'R':
            pos += 1
        else:
            l = pos
            while pos < n and s[pos] == 'L':
                pos += 1
            r = pos
            if (r - l) % 2 == 0:
                ans[l] = (r - l) // 2
                ans[r - 1] = (r - l) // 2
            else:
                ans[l] = (r - l) // 2 + 1
                ans[r - 1] = (r - l) // 2
    print(" ".join(map(str, ans)))
