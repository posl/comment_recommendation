def main():
    s = input()
    t = input()
    if len(s) > len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            print("Yes")
            return
        print("No")
        return
    print("Yes")
