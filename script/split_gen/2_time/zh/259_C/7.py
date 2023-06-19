def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        if s + s[0] == t:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
