def main():
    s = input()
    length = len(s)
    count = 0
    for i in range(length):
        if s[i] != s[length - i - 1]:
            count += 1
    if count == 0:
        if length % 2 == 0:
            print("YES")
        else:
            print("NO")
    elif count == 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()