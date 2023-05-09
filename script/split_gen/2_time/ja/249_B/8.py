def main():
    s = input()
    if s.isupper() or s.islower():
        print("No")
        return
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                print("No")
                return
    print("Yes")
