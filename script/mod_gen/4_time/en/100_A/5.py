def main():
    # input
    A, B = map(int, input().split())
    # compute
    # output
    if A <= 8 and B <= 8:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()