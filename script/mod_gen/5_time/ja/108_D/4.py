def main():
    L = int(input())
    print(2, 2 * L)
    for i in range(1, L):
        print(i, i + 1, 0)
        print(i, i + 1, 2 ** (i - 1))
    A = L.bit_length() - 1
    B = L - 2 ** A + 1
    for i in range(A):
        if (B >> i) & 1:
            print(A + 1, i + 1, 2 ** i)
    for i in range(A):
        if not (B >> i) & 1:
            print(A + 1, i + 1, 2 ** i)

if __name__ == '__main__':
    main()