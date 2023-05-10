def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(0, len(s)-1):
        if s[i] != t[i]:
            if s[i+1] == t[i] and s[i] == t[i+1]:
                print("Yes")
                return
            else:
                print("No")
                return
    print("No")
    return
