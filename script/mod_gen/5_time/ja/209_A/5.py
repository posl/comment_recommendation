def main():
    a,b = map(int, input().split())
    if b >= a:
        print(b - a + 1)
    else:
        print(0)

if __name__ == '__main__':
    main()