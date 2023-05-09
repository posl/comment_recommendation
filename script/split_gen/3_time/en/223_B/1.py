def main():
    s = input()
    smin = s
    smax = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < smin:
            smin = s
        if s > smax:
            smax = s
    print(smin)
    print(smax)
