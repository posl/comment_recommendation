def main():
    # Read from stdin
    a, b, c = map(int, input().split())
    # Print result to stdout
    print(int(a * b / 2))

if __name__ == '__main__':
    main()