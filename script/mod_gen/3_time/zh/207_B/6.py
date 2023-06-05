def main():
    a,b,c,d = map(int, input().split())
    if a < b:
        print(-1)
    else:
        if c*d <= b:
            print(-1)
        else:
            print((a + b - 1) // b - 1)

if __name__ == '__main__':
    main()