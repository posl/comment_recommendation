def main():
    # Read input
    N, M = [int(x) for x in input().split()]
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    # Count number of strings of S that end with a string of T
    count = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                count += 1
                break
    # Output result
    print(count)

if __name__ == '__main__':
    main()