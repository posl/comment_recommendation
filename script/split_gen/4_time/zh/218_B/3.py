def main():
    p = list(map(int, input().split()))
    s = [0] * 26
    for i in range(26):
        s[i] = chr(p[i] + 96)
    print(''.join(s))
