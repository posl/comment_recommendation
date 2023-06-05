def main():
    N = int(input())
    x = input().split()
    x = [int(i) for i in x]
    x_manhattan = 0
    x_euclidean = 0
    x_chebyshev = 0
    for i in x:
        x_manhattan += abs(i)
        x_euclidean += i**2
        if abs(i) > x_chebyshev:
            x_chebyshev = abs(i)
    x_euclidean = x_euclidean**0.5
    print(x_manhattan)
    print(x_euclidean)
    print(x_chebyshev)

if __name__ == '__main__':
    main()