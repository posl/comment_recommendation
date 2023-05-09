def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s.count(s[i]) != t.count(t[i]):
            print("No")
            return
    print("Yes")
