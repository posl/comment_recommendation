def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    print(1, 2, 0)
    print(2, 3, 0)
    print(3, 4, 0)
    print(1, 5, 0)
    print(2, 6, 0)
    print(3, 7, 0)
    print(4, 8, 0)
    print(5, 6, 1)
    print(6, 7, 1)
    print(7, 8, 1)
    for i in range(3, N):
        print(i, i+1, 0)
    for i in range(N, N+L-1):
        print(i, i+1, 1)

if __name__ == '__main__':
    main()