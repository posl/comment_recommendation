def main():
    s = input()
    c = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].isupper():
                c += 1
        else:
            if s[i].islower():
                c += 1
    if c == len(s):
        print("Yes")
    else:
        print("No")
main()
