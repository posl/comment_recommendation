def main():
    s = input()
    n = len(s)
    if s[:(n-1)//2] == s[:(n-1)//2][::-1] and s[(n+1)//2-1:] == s[(n+1)//2-1:][::-1]:
        print("Yes")
    else:
        print("No")
