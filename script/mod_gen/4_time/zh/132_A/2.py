def main():
    s = input()
    a = s[0]
    b = s[1]
    c = s[2]
    d = s[3]
    if((a == b and c == d and b != c) or (a == c and b == d and b != c) or (a == d and b == c and b != d)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()