def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        if ord(s[i]) > ord(t[i]):
            if ord(s[i]) - ord(t[i]) <= 13:
                continue
            else:
                print("No")
                return
        else:
            if ord(t[i]) - ord(s[i]) <= 13:
                continue
            else:
                print("No")
                return
    print("Yes")
    return
