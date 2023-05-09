def main():
    a, b, c, d = map(int, input().split())
    if b >= d:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()