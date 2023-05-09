def main():
    # Get input here
    h1, h2, h3, w1, w2, w3 = map(int, input().strip().split())
    # Calculate result here
    result = 0
    result = h1*h2*h3*w1*w2*w3
    # Print output here
    print(result)
main()

if __name__ == '__main__':
    main()