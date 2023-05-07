def main():
    s = input()
    if s in 'o' * 10 ** 5:
        print('Yes')
    elif s in 'x' * 10 ** 5:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()