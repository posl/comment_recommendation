def main():
    A, B = map(int, input().split())
    if (A * B) % 2 == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()