def main():
    # Get input here
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    # Calculate result here
    result = 0
    for i in range(h):
        result += s[i].count('#')
    # Print output here
    print(result)

if __name__ == '__main__':
    main()