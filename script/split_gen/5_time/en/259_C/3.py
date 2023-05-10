def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            if s == t:
                print("Yes")
                return
    print("No")
