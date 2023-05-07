def main():
    n, x = map(int, input().split())
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x <= n:
        print(s[x-1])
    else:
        print(s[(x-1)//n])
main()

if __name__ == '__main__':
    main()