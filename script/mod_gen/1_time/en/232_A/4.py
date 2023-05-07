def main():
    # Read input
    s = input()
    # Split string
    a, x, b = s.split('x')
    # Print output
    print(int(a) * int(b))

if __name__ == '__main__':
    main()