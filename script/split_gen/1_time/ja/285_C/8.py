def main():
    s = input()
    print(ord(s[0])-ord('A')+1+26*(len(s)-1))
