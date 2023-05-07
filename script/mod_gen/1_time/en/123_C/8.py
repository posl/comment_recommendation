def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # Find the smallest of A, B, C, D and E
    # The smallest of A, B, C, D and E is the minimum time needed to reach City 6
    smallest = min(A, B, C, D, E)
    # If N is smaller than the smallest of A, B, C, D and E, the minimum time needed to reach City 6 is N
    if N <= smallest:
        print(N)
    # If N is not smaller than the smallest of A, B, C, D and E, the minimum time needed to reach City 6 is N//smallest + 4
    else:
        print(N//smallest + 4)

if __name__ == '__main__':
    main()