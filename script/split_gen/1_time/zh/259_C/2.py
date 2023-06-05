def main():
    s = input()
    t = input()
    if len(s) < 2 or len(s) > 2*10**5 or len(t) < 2 or len(t) > 2*10**5:
        return
    if s == t:
        print("Yes")
        return
    i = 0
    while i < len(s):
        if i == len(s)-1:
            print("No")
            return
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            i += 2
        else:
            i += 1
    if s == t:
        print("Yes")
    else:
        print("No")
    return
