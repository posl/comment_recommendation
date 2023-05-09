def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N - 1):
        print(i, i + 2, 1)
    k = 2
    for i in range(1, N - 2):
        print(i, i + 3, k)
        k += 1
    for i in range(1, L):
        print(i, i + 1, 0)

if __name__ == '__main__':
    main()