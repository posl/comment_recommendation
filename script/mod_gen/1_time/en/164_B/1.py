def main():
    A, B, C, D = map(int, input().split())
    while A > 0 and C > 0:
        C -= B
        if C <= 0:
            print('Yes')
            return
        A -= D
    print('No')

if __name__ == '__main__':
    main()