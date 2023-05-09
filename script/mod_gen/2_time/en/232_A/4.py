def main():
    # read the input
    s = input()
    # split the input to get the numbers
    a, b = s.split('x')
    # convert the numbers to integers and multiply them
    print(int(a) * int(b))

if __name__ == '__main__':
    main()