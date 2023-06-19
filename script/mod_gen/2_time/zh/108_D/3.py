def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-1):
        print(i, i+2, L-i)
    print(1, 3, L)

if __name__ == '__main__':
    main()