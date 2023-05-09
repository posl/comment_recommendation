def main():
    s = input()
    for i in range(0, len(s)):
        if i % 2 == 0:
            if not s[i].isupper():
                print("No")
                return
        else:
            if not s[i].islower():
                print("No")
                return
    print("Yes")
