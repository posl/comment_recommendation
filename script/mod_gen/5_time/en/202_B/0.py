def main():
    s = input()
    s = s[::-1]
    s = s.replace('0', 'x')
    s = s.replace('1', '0')
    s = s.replace('x', '1')
    s = s.replace('6', 'x')
    s = s.replace('9', '6')
    s = s.replace('x', '9')
    print(s)

if __name__ == '__main__':
    main()