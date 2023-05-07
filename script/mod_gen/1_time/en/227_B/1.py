def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    if n == 1:
        print(1)
    elif n == 2:
        if s[0] == s[1]:
            print(1)
        else:
            print(2)
    else:
        if s[0] == s[1]:
            print(n-1)
        elif s[1] == s[2]:
            print(n-1)
        elif s[0] == s[2]:
            print(n-1)
        else:
            print(n)

if __name__ == '__main__':
    main()