def main():
    N = int(input())
    N = int(1.08 * N)
    if N < 206:
        print("Yay!")
    elif N == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()