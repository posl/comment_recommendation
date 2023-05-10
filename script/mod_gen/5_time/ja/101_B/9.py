def main():
    n = input()
    s = sum([int(i) for i in n])
    if int(n) % s == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()