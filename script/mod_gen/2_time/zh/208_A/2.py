def main():
    a, b = map(int, input().split())
    for i in range(1, a+1):
        if b <= i*6 and b >= i*1:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()