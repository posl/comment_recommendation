def main():
    s = input()
    if len(s) == len(set(s)):
        print(s[0])
    else:
        print(-1)
