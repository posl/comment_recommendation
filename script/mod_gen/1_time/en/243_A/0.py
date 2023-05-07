def main():
    v, a, b, c = map(int, input().split())
    if v <= a:
        print('F')
    elif v <= a + b:
        print('M')
    else:
        print('T')
main()

if __name__ == '__main__':
    main()