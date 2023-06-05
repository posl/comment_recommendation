def main():
    s = input()
    t = input()
    if s[0] == t[1] and s[1] == t[0] and len(s) == len(t):
        print("Yes")
    else:
        print("No")
