def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            print("No")
            return
        elif i % 2 != 0 and s[i].islower():
            print("No")
            return
    print("Yes")
    return
