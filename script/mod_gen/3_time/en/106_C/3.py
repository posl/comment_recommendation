def main():
    s = input()
    k = int(input())
    s = s.replace('1', '1 ')
    s = s.replace('2', '2 22 ')
    s = s.replace('3', '3 333 ')
    s = s.replace('4', '4 4444 ')
    s = s.replace('5', '5 55555 ')
    s = s.replace('6', '6 666666 ')
    s = s.replace('7', '7 7777777 ')
    s = s.replace('8', '8 88888888 ')
    s = s.replace('9', '9 999999999 ')
    s = s.split()
    print(s[k-1])

if __name__ == '__main__':
    main()