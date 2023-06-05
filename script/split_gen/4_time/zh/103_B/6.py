def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(0, len(s)):
        if s == t:
            print("Yes")
            return
        s = s[-1] + s[0:-1]
    print("No")
