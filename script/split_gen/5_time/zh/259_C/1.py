def main():
    s = input()
    t = input()
    if len(s) == len(t):
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i + 1] + s[i] + s[i + 1:]
                break
        if s == t:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
