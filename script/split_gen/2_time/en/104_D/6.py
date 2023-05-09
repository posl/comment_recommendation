def main():
    s = input()
    mod = 10 ** 9 + 7
    abc = [0, 0, 0]
    ans = 1
    for c in s:
        if c == '?':
            ans *= 3
            ans %= mod
            abc = [abc[0] * 3 + abc[1], abc[0] + abc[1] * 3 + abc[2], abc[1] + abc[2] * 3]
            abc[0] %= mod
            abc[1] %= mod
            abc[2] %= mod
        else:
            abc = [abc[0] * (c == 'A') + abc[1] * (c == 'B'), abc[0] * (c == 'B') + abc[1] * (c == 'C') + abc[2] * (c == 'A'), abc[1] * (c == 'A') + abc[2] * (c == 'B')]
    print((abc[2] * ans) % mod)
