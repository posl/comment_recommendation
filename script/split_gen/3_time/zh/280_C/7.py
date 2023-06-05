def main():
    s = input()
    t = input()
    for i in range(0, len(s)):
        if s[i] != t[i]:
            print(i + 1)
            break
