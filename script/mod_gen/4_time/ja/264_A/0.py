def main():
    l, r = map(int, input().split())
    s = input()
    print(s[l-1:r])

if __name__ == '__main__':
    main()