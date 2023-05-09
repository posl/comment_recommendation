def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            break
    else:
        print("Yes")
