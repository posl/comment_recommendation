def main():
    a,b,c,d = map(int, input().split())
    if a > b * d:
        print(-1)
    else:
        print((a + b - 1) // b)

if __name__ == '__main__':
    main()