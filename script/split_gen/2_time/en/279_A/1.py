def main():
    s = input()
    v = 0
    w = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v += 1
        else:
            w += 1
            ans += v
    print(ans)
