def main():
    N = int(input())
    if str(N) == str(N)[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()