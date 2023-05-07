def main():
    s = input()
    l = len(s)
    if s == s[::-1] and s[:(l-1)//2] == s[:(l-1)//2][::-1] and s[(l+3)//2-1:] == s[(l+3)//2-1:][::-1]:
        print("Yes")
    else:
        print("No")
