def main():
    s = input()
    t = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < t:
            t = s
    print(t)
    s = t
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s > t:
            t = s
    print(t)
