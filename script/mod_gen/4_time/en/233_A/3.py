def main():
    # input
    X, Y = map(int, input().split())
    # compute
    # output
    print(0 if X >= Y else Y - X)

if __name__ == '__main__':
    main()