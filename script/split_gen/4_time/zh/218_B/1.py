def main():
    p = list(map(int, input().split()))
    s = list(range(97, 123))
    for i in range(26):
        s[i] = chr(s[i])
    for i in range(26):
        s[p[i] - 1] = chr(97 + i)
    print(''.join(s))
