def main():
    s = input()
    t = 'o' + 'x' * 5 + 'o' + 'x' * 5 + 'o'
    if s in t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()