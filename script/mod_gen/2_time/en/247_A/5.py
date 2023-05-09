def main():
    s = input()
    for i in range(0, len(s) - 1):
        print(s[i], end = '')
    print('0')

if __name__ == '__main__':
    main()