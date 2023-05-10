def main():
    N = int(input())
    M = 2*N - 2
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-1):
        print(i, i+2, (1<<i-1))

if __name__ == '__main__':
    main()