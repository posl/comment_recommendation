def main():
    # read input
    N = int(input())
    # find the minimum number of moves
    if N % 2 == 0:
        print(N//2 - 1)
    else:
        print(N//2)

if __name__ == '__main__':
    main()