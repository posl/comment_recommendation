def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    M = min(A, B, C, D, E)
    print(((N + M - 1) // M) + 4)

if __name__ == '__main__':
    main()