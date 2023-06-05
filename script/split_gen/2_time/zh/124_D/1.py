def main():
    s = input()
    s1 = s[::2]
    s2 = s[1::2]
    s3 = s[1::2]
    s4 = s[::2]
    n1 = 0
    n2 = 0
    for i in range(len(s)):
        if s[i] == s1[i]:
            n1 += 1
        if s[i] == s2[i]:
            n2 += 1
    print(min(n1, n2))
