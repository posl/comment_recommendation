def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s) - 1):
        if s[i + 1:] + s[:i + 1] == t:
            print("Yes")
            return
    print("No")
