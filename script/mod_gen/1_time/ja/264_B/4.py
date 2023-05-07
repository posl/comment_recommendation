def main():
    r, c = map(int, input().split())
    if (r * c) % 2 == 0:
        print('white')
    else:
        print('black')
main()

if __name__ == '__main__':
    main()