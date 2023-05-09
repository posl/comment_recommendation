def main():
    s = input()
    for i in range(0, len(s)):
        print(s[i])
        print(s[0:i])
        print(s[i+1:len(s)])
        if s[i] not in s[0:i] and s[i] not in s[i+1:len(s)]:
            print(s[i])
            return
    print(-1)
    return
