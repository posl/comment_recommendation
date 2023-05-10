def main():
    a = [input() for _ in range(4)]
    if 'H' in a and '2B' in a and '3B' in a and 'HR' in a:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()