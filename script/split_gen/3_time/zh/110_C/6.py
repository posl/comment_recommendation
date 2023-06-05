def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                s[i], s[j] = s[j], s[i]
                if s == t:
                    print("Yes")
                    return
                s[i], s[j] = s[j], s[i]
        print("No")
