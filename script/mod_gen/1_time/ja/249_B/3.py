def main():
    s = input()
    a = 0
    b = 0
    for i in s:
        if i.isupper():
            a = 1
        if i.islower():
            b = 1
    if a == 1 and b == 1 and len(set(s)) == len(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()