def main():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print("No")
        return
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                print("No")
                return
        print("Yes")
