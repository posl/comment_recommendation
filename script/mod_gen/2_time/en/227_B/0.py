def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if s[0] + s[1] + s[2] == s[3] + s[4]:
        print(0)
    elif s[0] + s[1] + s[2] < s[3] + s[4]:
        print(0)
    elif s[0] + s[1] + s[2] > s[3] + s[4]:
        print(2)
    else:
        print(1)

if __name__ == '__main__':
    main()