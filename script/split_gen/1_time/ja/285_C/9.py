def main():
    s = input()
    print((ord(s[0])-64)*26**len(s) + (ord(s[1])-64) if len(s)==2 else ord(s[0])-64)
