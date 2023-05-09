def main():
    N = input()
    N = list(N)
    N = list(map(int, N))
    N.sort(reverse=True)
    N = list(map(str, N))
    N = ''.join(N)
    N = int(N)
    N1 = N
    N2 = 0
    for i in range(1, N):
        N1 = N1 // 10
        N2 = N2 * 10 + N % 10
        N = N // 10
        if N1 * N2 > N:
            break
    print(N1 * N2)

if __name__ == '__main__':
    main()