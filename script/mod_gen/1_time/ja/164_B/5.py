def main():
    A,B,C,D = map(int,input().split())
    while True:
        C -= B
        if C <= 0:
            print('Yes')
            return
        A -= D
        if A <= 0:
            print('No')
            return

if __name__ == '__main__':
    main()