def main():
    s = input()
    t = 'o' + s + 'o'
    if t == t[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()