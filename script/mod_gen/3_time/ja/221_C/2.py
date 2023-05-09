def main():
    N = input()
    N = [int(i) for i in N]
    N.sort(reverse=True)
    N1 = N[0]
    N2 = 0
    for i in range(1, len(N)):
        N2 += N[i] * (10 ** (i - 1))
    print(N1 * N2)

if __name__ == '__main__':
    main()