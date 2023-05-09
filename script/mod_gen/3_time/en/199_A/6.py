def main():
    # Read the input
    a, b, c = map(int, input().split())
    # Check if the condition holds
    if a**2 + b**2 < c**2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()