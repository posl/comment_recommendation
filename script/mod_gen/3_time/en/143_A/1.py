def main():
    a, b = map(int, input().split())
    if b >= a:
        print(0)
    else:
        print(a - b)

if __name__ == '__main__':
    main()