def main():
    # input
    N = int(input())
    # compute
    # output
    if N*1.08 < 206:
        print("Yay!")
    elif N*1.08 == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()