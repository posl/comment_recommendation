def main():
    N = int(input())
    tax = int(N * 1.08)
    if tax > 206:
        print(":(")
    elif tax < 206:
        print("Yay!")
    else:
        print("so-so")

if __name__ == '__main__':
    main()