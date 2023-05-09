def main():
    n = int(input())
    if 100 <= n <= 999:
        if '7' in str(n):
            print('Yes')
        else:
            print('No')
    else:
        print('Number is not three-digit')

if __name__ == '__main__':
    main()