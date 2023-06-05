def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1+s2+s3)
    if len(s)>10:
        print("UNSOLVABLE")
        return
    s = list(s)
    c = [0]*26
    for i in range(len(s)):
        c[ord(s[i])-ord('a')] = i
    if len(s)>9:
        for i in range(10):
            c[i] = i
    import itertools
    for p in itertools.permutations([i for i in range(len(s))]):
        if c[ord(s1[0])-ord('a')]!=0 and c[ord(s2[0])-ord('a')]!=0 and c[ord(s3[0])-ord('a')]!=0:
            n1 = n2 = n3 = 0
            for i in range(len(s1)):
                n1 = n1*10+c[ord(s1[i])-ord('a')]
            for i in range(len(s2)):
                n2 = n2*10+c[ord(s2[i])-ord('a')]
            for i in range(len(s3)):
                n3 = n3*10+c[ord(s3[i])-ord('a')]
            if n1+n2==n3:
                print(n1)
                print(n2)
                print(n3)
                return
    print("UNSOLVABLE")
