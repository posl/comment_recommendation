def main():
    n = int(input())
    if (n*1.08) < 206:
        print('Yay!')
    elif (n*1.08) > 206:
        print(':(')
    else:
        print('so-so')

if __name__ == '__main__':
    main()