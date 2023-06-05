def main():
    # input
    s = input()
    # compute
    s = s[::-1]
    s = s.replace('6', 'x')
    s = s.replace('9', '6')
    s = s.replace('x', '9')
    # output
    print(s)

if __name__ == '__main__':
    main()