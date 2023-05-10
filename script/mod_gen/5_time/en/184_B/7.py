def main():
    # Get input here
    n, x = map(int, input().strip().split())
    s = list(input().strip())
    # Calculate result here
    result = x
    for i in s:
        if i == 'o':
            result += 1
        else:
            if result > 0:
                result -= 1
    # Print output here
    print(result)

if __name__ == '__main__':
    main()