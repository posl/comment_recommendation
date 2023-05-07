def main():
    s = input()
    v = 0
    w = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v += 1
        if s[i] == 'w':
            w += 1
        if v > w:
            ans += 1
    print(ans)
