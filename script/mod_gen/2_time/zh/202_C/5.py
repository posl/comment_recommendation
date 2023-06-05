def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 'a')
    s = s.replace('9', 'b')
    s = s.replace('1', 'c')
    s = s.replace('a', '1')
    s = s.replace('b', '9')
    s = s.replace('c', '1')
    print(s)

if __name__ == '__main__':
    main()