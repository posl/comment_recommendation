def solve():
    s = input()
    if s.islower():
        print("No")
        return
    if s.isupper():
        print("No")
        return
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                print("No")
                return
    print("Yes")
