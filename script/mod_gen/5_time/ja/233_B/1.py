def main():
    l, r = map(int, input().split())
    s = input()
    s = list(s)
    s[l-1:r] = s[l-1:r][::-1]
    print("".join(s))

if __name__ == '__main__':
    main()