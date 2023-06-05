def main():
    n = int(input())
    p = int(1.08 * n)
    if p < 206:
        print("Yay!")
    elif p == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()