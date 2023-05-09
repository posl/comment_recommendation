def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        s1 = s[:i]
        s2 = s[len(s)-len(t)+i:]
        s3 = s1+s2
        if s3 == t:
            print("Yes")
        else:
            print("No")
