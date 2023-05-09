def main():
    n = int(input())
    if n%4 == 0 or n%7 == 0 or n%11 == 0:
        print('Yes')
        exit()
    for i in range(1, n//4+1):
        for j in range(1, n//7+1):
            if i*4 + j*7 == n:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()