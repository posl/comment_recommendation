def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            if s[:i-1] + s[i+1:] == t:
                print("Yes")
                exit()
    print("No")
