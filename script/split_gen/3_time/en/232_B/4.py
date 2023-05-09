def main():
    s = input()
    t = input()
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i:] + s[:i] == t:
                print("Yes")
                return
        print("No")
    else:
        print("No")
