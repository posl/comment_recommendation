def main():
    s = input()
    t = input()
    
    if s == t:
        print("Yes")
        return
    
    if len(s) > len(t):
        print("No")
        return
    
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] == t[i+1] and s[i+1] == t[i+2]:
                print("Yes")
                return
            else:
                print("No")
                return
    
    print("Yes")
