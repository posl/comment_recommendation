def main():
    n = int(input())
    if n % sum(list(map(int, list(str(n))))) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()