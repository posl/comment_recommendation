def main():
    s = input()
    d = [0] * 13
    d[0] = 1
    for c in s:
        if c == '?':
            d = [sum(d[(j - k) % 13] for k in range(10)) % 1000000007 for j in range(13)]
        else:
            d = [d[(j - int(c)) % 13] for j in range(13)]
    print(d[5])
