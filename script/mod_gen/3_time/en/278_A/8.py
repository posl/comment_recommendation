def main():
    # Get input here
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # Calculate result here
    for i in range(k):
        a.append(a.pop(0))
    # Print output here
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()