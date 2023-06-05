def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 't')
    s = s.replace('9', '6')
    s = s.replace('t', '9')
    s = s.replace('1', 't')
    s = s.replace('0', '1')
    s = s.replace('t', '0')
    print(s)

if __name__ == '__main__':
    main()