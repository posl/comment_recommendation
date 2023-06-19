def main():
    str = input()
    num = str.split(' ')
    for i in range(26):
        print(chr(int(num[i])+96), end='')

if __name__ == '__main__':
    main()