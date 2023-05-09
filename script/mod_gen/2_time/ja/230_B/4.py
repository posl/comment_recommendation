def main():
    s = input()
    t = 'o' + 'x' * 10**5
    if s in t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()