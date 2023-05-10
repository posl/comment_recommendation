def main():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0 or n % 11 == 0:
        print('Yes')
    else:
        for i in range(1, 10):
            for j in range(1, 10):
                if 4*i + 7*j == n:
                    print('Yes')
                    return
        print('No')

if __name__ == '__main__':
    main()