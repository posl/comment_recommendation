def main():
    n,x = map(int, input().split())
    s = ''
    for i in range(65,91):
        s += chr(i) * n
    print(s[x-1])

if __name__ == '__main__':
    main()