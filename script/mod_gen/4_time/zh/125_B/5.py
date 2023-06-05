def main():
    # N = 3
    # V = [10, 2, 5]
    # C = [6, 3, 4]
    # N = 4
    # V = [13, 21, 6, 19]
    # C = [11, 30, 6, 15]
    # N = 1
    # V = [1]
    # C = [50]
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    print(max(x - y for x, y in zip(V, C) if x > y))

if __name__ == '__main__':
    main()