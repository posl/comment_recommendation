def problem104_b():
    s = input()
    if s[0] != 'A':
        print("WA")
        return
    if s[2:-1].count('C') != 1:
        print("WA")
        return
    for i in range(1,len(s)):
        if s[i] != 'C' and s[i].isupper():
            print("WA")
            return
    print("AC")
