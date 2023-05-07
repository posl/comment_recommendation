def main():
    # Get input here
    n = int(input())
    s = [input() for i in range(n)]
    # Calculate result here
    result = 'Yes' if s.count('For') > s.count('Against') else 'No'
    # Print result here
    print(result)
main()

if __name__ == '__main__':
    main()