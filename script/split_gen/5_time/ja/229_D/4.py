def main():
    s = input()
    k = int(input())
    n = len(s)
    if n == 1:
        print(k//2)
        return
    if n == 2:
        if s[0] == s[1]:
            print(k)
            return
        else:
            print(0)
            return
    if s[0] == s[n-1]:
        if s[0] == s[n-2]:
            if s[0] == s[n-3]:
                print((k//2)*3+1)
                return
            else:
                print((k//2)*3)
                return
        else:
            print((k//2)*2)
            return
    else:
        print((k//2)*2)
        return
