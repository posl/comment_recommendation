def main():
    N = int(input())
    x = list(map(int, input().split()))
    # Manhattan distance
    print(sum(map(abs, x)))
    # Euclidian distance
    print((sum(map(lambda x: x**2, x)))**0.5)
    # Chebyshev distance
    print(max(map(abs, x)))

if __name__ == '__main__':
    main()