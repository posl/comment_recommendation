def main():
    # input
    X, A = map(int, input().split())
    # output
    if X < A:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()