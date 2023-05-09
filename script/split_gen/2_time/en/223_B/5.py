def main():
    s = input()
    l = len(s)
    s = s + s
    smin = s[0:l]
    smax = s[0:l]
    for i in range(1,l):
        if s[i:i+l] < smin:
            smin = s[i:i+l]
        if s[i:i+l] > smax:
            smax = s[i:i+l]
    print(smin)
    print(smax)
