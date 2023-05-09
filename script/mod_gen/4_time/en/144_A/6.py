def main():
    # Take input
    a, b = map(int, input().split())
    # Calculate and print result
    if 1 <= a <= 9 and 1 <= b <= 9:
        print(a * b)
    else:
        print(-1)

if __name__ == '__main__':
    main()