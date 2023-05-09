def main():
    s = input()
    mod = 10**9 + 7
    count = [0] * 8
    for c in s:
        if c == 'c':
            count[0] += 1
        elif c == 'h':
            count[1] += count[0]
        elif c == 'o':
            count[2] += count[1]
        elif c == 'k':
            count[3] += count[2]
        elif c == 'u':
            count[4] += count[3]
        elif c == 'd':
            count[5] += count[4]
        elif c == 'a':
            count[6] += count[5]
        elif c == 'i':
            count[7] += count[6]
    print(count[7] % mod)
