def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    if len(s) == len(t):
        print("No")
        return
    if s[0] != t[0]:
        print("No")
        return
    if s[-1] != t[-1]:
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            break
    for j in range(len(s)-1,0,-1):
        if s[j] != t[j]:
            break
    if s[i:j+1] == t[i+1:j+2]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()